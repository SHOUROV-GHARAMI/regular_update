import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'online_library.settings')
django.setup()

from library.models import Book, Category

print(f'Total books in database: {Book.objects.count()}')
print(f'Total categories in database: {Category.objects.count()}')
print('\nAll books in the library:')
for book in Book.objects.all().order_by('title'):
    print(f'- {book.title} by {book.author} ({book.category.name})')