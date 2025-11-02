from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from library.models import Book, Review
import random


class Command(BaseCommand):
    help = 'Add sample reviews to test dynamic features'

    def handle(self, *args, **options):
        # Get existing users and books
        users = User.objects.all()
        books = Book.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create some users first.'))
            return
            
        if not books.exists():
            self.stdout.write(self.style.ERROR('No books found. Please add some books first.'))
            return

        # Sample review comments
        review_comments = [
            "Absolutely fantastic read! Couldn't put it down.",
            "Great book with compelling characters and plot.",
            "Highly recommend this to anyone interested in the genre.",
            "Well-written and engaging from start to finish.",
            "A masterpiece that will stay with you long after reading.",
            "Excellent storytelling and character development.",
            "This book exceeded my expectations in every way.",
            "A thought-provoking and insightful read.",
            "Perfect blend of entertainment and education.",
            "One of the best books I've read this year.",
            "Captivating story that keeps you hooked.",
            "Beautiful prose and meaningful themes.",
            "An emotional rollercoaster worth taking.",
            "Brilliantly crafted with attention to detail.",
            "This book changed my perspective on many things."
        ]

        reviews_added = 0
        
        # Add reviews for random books by random users
        for i in range(min(15, len(books) * 2)):  # Add up to 15 reviews
            user = random.choice(users)
            book = random.choice(books)
            
            # Check if this user already reviewed this book
            if not Review.objects.filter(user=user, book=book).exists():
                rating = random.randint(3, 5)  # Give mostly good ratings
                comment = random.choice(review_comments)
                
                Review.objects.create(
                    user=user,
                    book=book,
                    rating=rating,
                    comment=comment
                )
                
                reviews_added += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Added review: {book.title} - {rating} stars by {user.username}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nCompleted! Added {reviews_added} new reviews.')
        )
        
        # Display current statistics
        total_books = Book.objects.count()
        total_users = User.objects.count()
        total_reviews = Review.objects.count()
        
        self.stdout.write('\nCurrent Library Statistics:')
        self.stdout.write(f'- Total Books: {total_books}')
        self.stdout.write(f'- Total Users: {total_users}')
        self.stdout.write(f'- Total Reviews: {total_reviews}')