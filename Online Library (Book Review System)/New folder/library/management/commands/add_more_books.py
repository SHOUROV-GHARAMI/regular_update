from django.core.management.base import BaseCommand
from library.models import Book, Category
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Add 10 more books to the library database'

    def handle(self, *args, **options):
        # Get or create categories
        fiction, _ = Category.objects.get_or_create(name='Fiction')
        non_fiction, _ = Category.objects.get_or_create(name='Non-Fiction')
        mystery, _ = Category.objects.get_or_create(name='Mystery')
        romance, _ = Category.objects.get_or_create(name='Romance')
        thriller, _ = Category.objects.get_or_create(name='Thriller')
        biography, _ = Category.objects.get_or_create(name='Biography')
        history, _ = Category.objects.get_or_create(name='History')
        
        # List of 10 new books to add
        books_data = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'description': 'A classic American novel set in the Jazz Age, exploring themes of wealth, love, and the American Dream.',
                'category': fiction,
                'publication_date': '1925-04-10'
            },
            {
                'title': 'Sapiens: A Brief History of Humankind',
                'author': 'Yuval Noah Harari',
                'isbn': '9780062316097',
                'description': 'A thought-provoking exploration of human history from the Stone Age to the present.',
                'category': non_fiction,
                'publication_date': '2011-01-01'
            },
            {
                'title': 'The Girl with the Dragon Tattoo',
                'author': 'Stieg Larsson',
                'isbn': '9780307454546',
                'description': 'A gripping mystery thriller about a journalist and a hacker investigating a decades-old disappearance.',
                'category': mystery,
                'publication_date': '2005-08-01'
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'isbn': '9780141439518',
                'description': 'A timeless romance novel about Elizabeth Bennet and Mr. Darcy in 19th-century England.',
                'category': romance,
                'publication_date': '1813-01-28'
            },
            {
                'title': 'Gone Girl',
                'author': 'Gillian Flynn',
                'isbn': '9780307588371',
                'description': 'A psychological thriller about a marriage gone terribly wrong when a wife disappears.',
                'category': thriller,
                'publication_date': '2012-06-05'
            },
            {
                'title': 'Steve Jobs',
                'author': 'Walter Isaacson',
                'isbn': '9781451648539',
                'description': 'The definitive biography of Apple co-founder Steve Jobs, based on extensive interviews.',
                'category': biography,
                'publication_date': '2011-10-24'
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'isbn': '9780316769174',
                'description': 'A coming-of-age story following teenager Holden Caulfield in New York City.',
                'category': fiction,
                'publication_date': '1951-07-16'
            },
            {
                'title': 'A Brief History of Time',
                'author': 'Stephen Hawking',
                'isbn': '9780553380163',
                'description': 'An accessible exploration of cosmology and the nature of time by renowned physicist Stephen Hawking.',
                'category': non_fiction,
                'publication_date': '1988-04-01'
            },
            {
                'title': 'The Guns of August',
                'author': 'Barbara Tuchman',
                'isbn': '9780345476098',
                'description': 'A Pulitzer Prize-winning account of the first month of World War I.',
                'category': history,
                'publication_date': '1962-01-01'
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'isbn': '9780062315007',
                'description': 'A philosophical novel about a young shepherd who travels to Egypt in search of treasure.',
                'category': fiction,
                'publication_date': '1988-01-01'
            }
        ]

        # Add books to database
        books_added = 0
        for book_data in books_data:
            # Check if book already exists by ISBN
            if not Book.objects.filter(isbn=book_data['isbn']).exists():
                Book.objects.create(**book_data)
                books_added += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added: {book_data["title"]} by {book_data["author"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Book already exists: {book_data["title"]} by {book_data["author"]}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nCompleted! Added {books_added} new books to the library.')
        )