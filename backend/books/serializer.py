from rest_framework.serializers import ModelSerializer
from books.models import Books, Category
from rest_framework import serializers


class BookSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    file = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = '__all__'

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None

    def get_file(self, obj):
        if obj.file:
            return self.context['request'].build_absolute_uri(obj.file.url)
        return None

    def get_category(self, obj):
        return {
            'name': obj.category.name,
            'slug': obj.category.slug
        }
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
class YourCombinedSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)
    books = BookSerializer(many=True)

    def to_representation(self, instance):
        # Convert the queryset into dictionary format
        data = super().to_representation(instance)

        # Rename the categories and books keys to match the JSON structure you want
        combined_data = {
            'categories': data['categories'],
            'books': data['books']
        }

        return combined_data
