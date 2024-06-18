from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static

from books.views import BookView, CategoryView, BookByCategoryView, BookDetailView

# === ROUTERS ===
router = routers.SimpleRouter()
router.register('api/category', CategoryView)
router.register('api/books', BookView)

# === URL_PATTERNS =====
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/<slug:category_slug>/', BookByCategoryView.as_view(), name='books_by_category'),
    path('api/books/<slug:category_slug>/<int:id_book>', BookDetailView.as_view(), name='book_detail')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls