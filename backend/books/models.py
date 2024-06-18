from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.slug])


class Books(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='books',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255, db_index=True)
    slug = models.CharField(max_length=255, db_index=True, unique=True)
    author = models.CharField(max_length=150, db_index=True, null=True)
    date = models.CharField(max_length=150, db_index=True, null=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True, max_length=500)
    save_file = models.FileField(upload_to='products/', default='default_filename.txt', max_length=500)
    file = models.FileField(upload_to='books/%Y/%m/%d', blank=True, max_length=500)
    description = models.TextField(max_length=5000, blank=True)
    created = models.DateTimeField(default=timezone.now)
    uploaded = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        indexes = [models.Index(fields=['name', 'slug'])]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        if not self.uploaded:
            self.uploaded = timezone.now()
        super().save(*args, **kwargs)
