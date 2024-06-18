from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from books.models import Books, Category
from books.serializer import BookSerializer, CategorySerializer, YourCombinedSerializer
from rest_framework.response import Response
from django.db.models import Q
from random import sample


def product_page(request):
    return render(request, 'books/_page.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Books.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'books/books_page.html',
                  {'category': category,
                   'categories': categories,
                   'products': products
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Books, id=id, slug=slug, available=True)
    return render(request, 'books/books_detail.html', {'product': product})


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # Get query parameters
        limit = self.request.query_params.get('_limit', None)
        start = self.request.query_params.get('_start', None)
        search_query = self.request.query_params.get('_search', None)
        random_books = self.request.query_params.get('_random', None)
        # Set default values for limit and start
        try:
            limit = int(limit) if limit else 12
            start = int(start) if start else 0
        except ValueError:
            return Response({'error': 'Invalid limit or start parameter'}, status=400)
        # Apply search filter if search_query is provided
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if random_books == 'true':  # Check if _random parameter is set to 'true'
            queryset = queryset.order_by('?')  # Randomize the order of the queryset
            queryset = list(queryset)  # Convert queryset to a list
            queryset = sample(queryset, min(limit, len(queryset)))  # Sample the queryset to get random books

        # Apply limit and start
        queryset = queryset[start:start + limit]
        return queryset

# class BookByCategoryView(APIView):
#     def get(self, request, category_slug):
#         # Get the category object by slug
#         category = get_object_or_404(Category, slug=category_slug)
#
#         # Get query parameters
#         limit = request.query_params.get('_limit', None)
#         start = request.query_params.get('_start', None)
#         search_query = request.query_params.get('_search', None)
#         random_books = request.query_params.get('_random', None)
#
#         # Set default values for limit and start
#         try:
#             limit = int(limit) if limit else 12
#             start = int(start) if start else 0
#         except ValueError:
#             return Response({'error': 'Invalid limit or start parameter'}, status=400)
#
#         if random_books == 'true':
#             # If random_books parameter is set, return random books
#             queryset = Books.objects.filter(category=category)
#             queryset = queryset.order_by('?')
#             queryset = list(queryset)
#             queryset = sample(queryset, min(limit, len(queryset)))
#         else:
#             # If search_query is provided, search both categories and books by name
#             queryset = Category.objects.filter(
#                 Q(name__icontains=search_query) | Q(slug__icontains=search_query)
#             ) | Books.objects.filter(
#                 Q(name__icontains=search_query) | Q(slug__icontains=search_query),
#                 category=category
#             )
#
#             # Apply limit and start
#             queryset = queryset[start:start + limit]
#
#         # Serialize the data with request object in context
#         serializer = YourCombinedSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

class BookByCategoryView(APIView):
    def get(self, request, category_slug):
        # Get the category object by slug
        category = get_object_or_404(Category, slug=category_slug)

        # Get query parameters
        limit = request.query_params.get('_limit', None)
        start = request.query_params.get('_start', None)
        search_query = request.query_params.get('_search', None)
        random_books = request.query_params.get('_random', None)

        # Set default values for limit and start
        try:
            limit = int(limit) if limit else 12
            start = int(start) if start else 0
        except ValueError:
            return Response({'error': 'Invalid limit or start parameter'}, status=400)

        # Filter books by category
        books = Books.objects.filter(category=category)

        # Apply search filter if search_query is provided
        if search_query:
            books = books.filter(name__icontains=search_query)

        if random_books == 'true':
            books = books.order_by('?')
            books = list(books)
            books = sample(books, min(limit, len(books)))

        # Apply limit and start
        books = books[start:start + limit]

        # Serialize the data with request object in context
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)


class BookDetailView(APIView):
    def get(self, request, category_slug, id_book):
        # Get the category object by slug
        category = get_object_or_404(Category, slug=category_slug)

        # Get the book object by id within the specified category
        book = get_object_or_404(Books, id=id_book, category__slug=category_slug, available=True)

        # Serialize the book data along with category details
        serializer = BookSerializer(book, context={'request': request})
        data = serializer.data
        data['category'] = {
            'name': category.name,
            'slug': category.slug
        }

        return Response(data)
