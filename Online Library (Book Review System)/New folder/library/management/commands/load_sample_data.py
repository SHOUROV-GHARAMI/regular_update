from django.core.management.base import BaseCommand
from library.models import Category, Book
from django.contrib.auth.models import User
from datetime import date


class Command(BaseCommand):
    help = 'Load sample data for the Online Library'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create categories
        categories_data = [
            {'name': 'Fiction', 'description': 'Novels and fictional stories'},
            {'name': 'Science Fiction', 'description': 'Futuristic and speculative fiction'},
            {'name': 'Mystery', 'description': 'Mystery and detective novels'},
            {'name': 'Romance', 'description': 'Romantic novels and stories'},
            {'name': 'Biography', 'description': 'Life stories of real people'},
            {'name': 'Self-Help', 'description': 'Personal development and improvement'},
            {'name': 'Technology', 'description': 'Books about technology and programming'},
            {'name': 'History', 'description': 'Historical books and accounts'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create books
        books_data = [
            {
                'title': 'The Great Adventure',
                'author': 'John Smith',
                'category': 'Fiction',
                'description': 'An epic tale of courage and friendship in a magical world.',
                'isbn': '9781234567890',
                'publication_date': date(2020, 5, 15),
            },
            {
                'title': 'Cyberpunk 2087',
                'author': 'Jane Doe',
                'category': 'Science Fiction',
                'description': 'A thrilling journey through a dystopian future where technology rules.',
                'isbn': '9781234567891',
                'publication_date': date(2021, 8, 20),
            },
            {
                'title': 'The Missing Diamond',
                'author': 'Detective Brown',
                'category': 'Mystery',
                'description': 'A gripping mystery involving a stolen diamond and unexpected twists.',
                'isbn': '9781234567892',
                'publication_date': date(2019, 12, 10),
            },
            {
                'title': 'Love in Paris',
                'author': 'Marie Claire',
                'category': 'Romance',
                'description': 'A beautiful love story set in the romantic city of Paris.',
                'isbn': '9781234567893',
                'publication_date': date(2022, 2, 14),
            },
            {
                'title': 'Steve Jobs: The Innovator',
                'author': 'Tech Writer',
                'category': 'Biography',
                'description': 'The inspiring life story of Apple co-founder Steve Jobs.',
                'isbn': '9781234567894',
                'publication_date': date(2018, 10, 5),
            },
            {
                'title': '7 Habits of Highly Effective People',
                'author': 'Stephen Covey',
                'category': 'Self-Help',
                'description': 'A powerful book about developing good habits and personal effectiveness.',
                'isbn': '9781234567895',
                'publication_date': date(1989, 8, 15),
            },
            {
                'title': 'Python Programming Mastery',
                'author': 'Code Master',
                'category': 'Technology',
                'description': 'Comprehensive guide to mastering Python programming language.',
                'isbn': '9781234567896',
                'publication_date': date(2023, 1, 1),
            },
            {
                'title': 'World War II Chronicles',
                'author': 'History Scholar',
                'category': 'History',
                'description': 'Detailed account of events during World War II.',
                'isbn': '9781234567897',
                'publication_date': date(2020, 11, 11),
            },
            {
                'title': 'The Art of Cooking',
                'author': 'Chef Gordon',
                'category': 'Self-Help',
                'description': 'Learn the fundamentals of cooking with this comprehensive guide.',
                'isbn': '9781234567898',
                'publication_date': date(2021, 6, 1),
            },
            {
                'title': 'Space Odyssey',
                'author': 'Arthur C. Clarke',
                'category': 'Science Fiction',
                'description': 'A classic science fiction novel about space exploration.',
                'isbn': '9781234567899',
                'publication_date': date(1968, 4, 3),
            },
        ]

        for book_data in books_data:
            category = categories[book_data['category']]
            book, created = Book.objects.get_or_create(
                title=book_data['title'],
                defaults={
                    'author': book_data['author'],
                    'category': category,
                    'description': book_data['description'],
                    'isbn': book_data['isbn'],
                    'publication_date': book_data['publication_date'],
                }
            )
            if created:
                self.stdout.write(f'Created book: {book.title}')

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully loaded sample data: '
                f'{Category.objects.count()} categories, '
                f'{Book.objects.count()} books'
            )
        )