# Generated by Django 4.2.3 on 2024-04-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_books_description_alter_books_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='save_file',
            field=models.FileField(default='default_filename.txt', max_length=500, upload_to='products/'),
        ),
    ]
