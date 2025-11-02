from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book, Category, Review
from .forms import ReviewForm, BookForm, CategoryForm, UserEditForm, AdminUserCreationForm


def home(request):
    """Home page with featured books and dynamic statistics"""
    # Get latest 6 books for display
    featured_books = Book.objects.all().order_by('-created_at')[:6]
    
    # Get all categories
    categories = Category.objects.all()
    
    # Calculate dynamic statistics
    total_books = Book.objects.count()
    total_categories = Category.objects.count()
    total_users = User.objects.count()
    total_reviews = Review.objects.count()
    
    # Get recent activity
    recent_reviews = Review.objects.all().order_by('-created_at')[:3]
    newest_books = Book.objects.all().order_by('-created_at')[:3]
    
    return render(request, 'library/home.html', {
        'books': featured_books,
        'categories': categories,
        'total_books': total_books,
        'total_categories': total_categories,
        'total_users': total_users,
        'total_reviews': total_reviews,
        'recent_reviews': recent_reviews,
        'newest_books': newest_books,
    })


def book_list(request):
    """List all books with search and filter functionality"""
    books = Book.objects.all()
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query)
        )
    
    # Category filter
    category_filter = request.GET.get('category')
    if category_filter:
        books = books.filter(category__id=category_filter)
    
    # Pagination
    paginator = Paginator(books, 12)  # Show 12 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'library/book_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_filter
    })


def book_detail(request, pk):
    """Book detail page with reviews"""
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    user_review = None
    
    if request.user.is_authenticated:
        try:
            user_review = Review.objects.get(book=book, user=request.user)
        except Review.DoesNotExist:
            user_review = None
    
    return render(request, 'library/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'user_review': user_review
    })


@login_required
def add_review(request, pk):
    """Add a review for a book"""
    book = get_object_or_404(Book, pk=pk)
    
    # Check if user already reviewed this book
    existing_review = Review.objects.filter(book=book, user=request.user).first()
    if existing_review:
        messages.error(request, 'You have already reviewed this book.')
        return redirect('library:book_detail', pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            messages.success(request, 'Your review has been added successfully!')
            return redirect('library:book_detail', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'library/add_review.html', {
        'form': form,
        'book': book
    })


@login_required
def edit_review(request, pk):
    """Edit an existing review"""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully!')
            return redirect('library:book_detail', pk=review.book.pk)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'library/edit_review.html', {
        'form': form,
        'review': review
    })


@login_required
def delete_review(request, pk):
    """Delete a review"""
    review = get_object_or_404(Review, pk=pk, user=request.user)
    
    if request.method == 'POST':
        book_pk = review.book.pk
        review.delete()
        messages.success(request, 'Your review has been deleted successfully!')
        return redirect('library:book_detail', pk=book_pk)
    
    return render(request, 'library/delete_review.html', {
        'review': review
    })


def books_by_category(request, category_id):
    """List books by category"""
    category = get_object_or_404(Category, pk=category_id)
    books = Book.objects.filter(category=category)
    
    # Pagination
    paginator = Paginator(books, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'library/books_by_category.html', {
        'category': category,
        'page_obj': page_obj
    })


# Admin Views
def is_admin(user):
    """Check if user is admin (superuser or staff)"""
    return user.is_authenticated and (user.is_superuser or user.is_staff)


@user_passes_test(is_admin)
def admin_dashboard(request):
    """Admin dashboard with statistics"""
    total_books = Book.objects.count()
    total_users = User.objects.count()
    total_reviews = Review.objects.count()
    total_categories = Category.objects.count()
    
    recent_books = Book.objects.all().order_by('-created_at')[:5]
    recent_users = User.objects.all().order_by('-date_joined')[:5]
    recent_reviews = Review.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_books': total_books,
        'total_users': total_users,
        'total_reviews': total_reviews,
        'total_categories': total_categories,
        'recent_books': recent_books,
        'recent_users': recent_users,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'library/admin/dashboard.html', context)


@user_passes_test(is_admin)
def admin_users(request):
    """Admin view to manage users"""
    users = User.objects.all().order_by('-date_joined')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) | 
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'library/admin/users.html', {
        'page_obj': page_obj,
        'search_query': search_query
    })


@user_passes_test(is_admin)
def admin_delete_user(request, user_id):
    """Delete a user"""
    user_to_delete = get_object_or_404(User, id=user_id)
    
    # Prevent admin from deleting themselves
    if user_to_delete == request.user:
        messages.error(request, "You cannot delete your own account!")
        return redirect('library:admin_users')
    
    # Prevent deletion of other superusers
    if user_to_delete.is_superuser and not request.user.is_superuser:
        messages.error(request, "You cannot delete a superuser!")
        return redirect('library:admin_users')
    
    if request.method == 'POST':
        username = user_to_delete.username
        user_to_delete.delete()
        messages.success(request, f"User '{username}' has been deleted successfully!")
        return redirect('library:admin_users')
    
    return render(request, 'library/admin/confirm_delete_user.html', {
        'user_to_delete': user_to_delete
    })


@user_passes_test(is_admin)
def admin_edit_user(request, user_id):
    """Edit user information"""
    user_to_edit = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user_to_edit)
        if form.is_valid():
            form.save()
            messages.success(request, f"User '{user_to_edit.username}' has been updated successfully!")
            return redirect('library:admin_users')
    else:
        form = UserEditForm(instance=user_to_edit)
    
    return render(request, 'library/admin/edit_user.html', {
        'form': form,
        'user_to_edit': user_to_edit
    })


@user_passes_test(is_admin)
def admin_add_user(request):
    """Add new user"""
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"User '{user.username}' has been created successfully!")
            return redirect('library:admin_users')
    else:
        form = AdminUserCreationForm()
    
    return render(request, 'library/admin/add_user.html', {'form': form})


@user_passes_test(is_admin)
def admin_books(request):
    """Admin view to manage books"""
    books = Book.objects.all().order_by('-created_at')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query)
        )
    
    # Category filter
    category_filter = request.GET.get('category')
    if category_filter:
        books = books.filter(category__id=category_filter)
    
    categories = Category.objects.all()
    
    # Pagination
    paginator = Paginator(books, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'library/admin/books.html', {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_filter
    })


@user_passes_test(is_admin)
def admin_add_book(request):
    """Add new book"""
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f"Book '{book.title}' has been added successfully!")
            return redirect('library:admin_books')
    else:
        form = BookForm()
    
    return render(request, 'library/admin/add_book.html', {'form': form})


@user_passes_test(is_admin)
def admin_edit_book(request, book_id):
    """Edit book information"""
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f"Book '{book.title}' has been updated successfully!")
            return redirect('library:admin_books')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'library/admin/edit_book.html', {
        'form': form,
        'book': book
    })


@user_passes_test(is_admin)
def admin_delete_book(request, book_id):
    """Delete a book"""
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f"Book '{title}' has been deleted successfully!")
        return redirect('library:admin_books')
    
    return render(request, 'library/admin/confirm_delete_book.html', {'book': book})


@user_passes_test(is_admin)
def admin_categories(request):
    """Admin view to manage categories"""
    categories = Category.objects.all().order_by('name')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        categories = categories.filter(name__icontains=search_query)
    
    return render(request, 'library/admin/categories.html', {
        'categories': categories,
        'search_query': search_query
    })


@user_passes_test(is_admin)
def admin_add_category(request):
    """Add new category"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f"Category '{category.name}' has been added successfully!")
            return redirect('library:admin_categories')
    else:
        form = CategoryForm()
    
    return render(request, 'library/admin/add_category.html', {'form': form})


@user_passes_test(is_admin)
def admin_edit_category(request, category_id):
    """Edit category information"""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f"Category '{category.name}' has been updated successfully!")
            return redirect('library:admin_categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'library/admin/edit_category.html', {
        'form': form,
        'category': category
    })


@user_passes_test(is_admin)
def admin_delete_category(request, category_id):
    """Delete a category"""
    category = get_object_or_404(Category, id=category_id)
    
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f"Category '{name}' has been deleted successfully!")
        return redirect('library:admin_categories')
    
    return render(request, 'library/admin/confirm_delete_category.html', {'category': category})
