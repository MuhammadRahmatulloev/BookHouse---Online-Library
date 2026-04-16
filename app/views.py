from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Publisher, Book, UserModel
from .filter import BookFilter  
from django.db import models


# def search_django(request):
#     query = request.GET.get('q', '')
#     products = {'products': Product.objects.filter(name__icontains=query), 'query': query}
#     return render()


def get_current_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    return UserModel.objects.filter(id=user_id).first()


def stats_view(request):
    book_stats = Book.objects.aggregate(
        total_books=models.Count('id'),
        total_price=models.Sum('price'),
        average_price=models.Avg('price'),
        max_price=models.Max('price'),
        min_price=models.Min('price'),)
    
    authors = Author.objects.annotate(
        num_books=models.Count('book'),
        avg_book_price=models.Avg('book__price'),
        max_book_price=models.Max('book__price'),)
    return render(request, 'stats.html', {'stats': book_stats, 'authors': authors,})


def category_list_view(request):
    if not get_current_user(request):
        return redirect('login')
    
    categories = Category.objects.all()

    q = request.GET.get('q')
    desc = request.GET.get('desc')
    if q:
        categories = categories.filter(name__icontains=q)
    if desc:
        categories = categories.filter(description__icontains=desc)

    return render(request, 'category_list.html', {'categories': categories})


def category_detail_view(request, pk):
    category = get_object_or_404(Category, id=pk)
    return render(request, 'category_detail.html', {'category': category})


def category_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Category.objects.create(name=name, description=description)
        return redirect('category_list')

    return render(request, 'category_create.html')


def category_update_view(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        category.name = name
        category.description = description
        category.save()
        return redirect('category_detail', pk=category.id)

    return render(request, 'category_update.html', {'category': category})


def category_delete_view(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'category_delete.html', {'category': category})


# def author_list_view(request):
#     authors = Author.objects.all()

#     search = request.GET.get('search')
#     if search:
#         authors = authors.filter(full_name__icontains=search) | authors.filter(email__icontains=search)

#     return render(request, 'author_list.html', {'authors': authors})


def author_list_view(request):
    if not get_current_user(request):
        return redirect('login')
    
    authors = Author.objects.prefetch_related('book_set')

    search = request.GET.get('search')
    if search:
        authors = authors.filter(full_name__icontains=search) | authors.filter(email__icontains=search)

    return render(request, 'author_list.html', {'authors': authors})


def author_detail_view(request, pk):
    author = get_object_or_404(Author, id=pk)
    return render(request, 'author_detail.html', {'author': author})


def author_create_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        photo = request.FILES.get('photo')
        Author.objects.create(full_name=full_name, email=email, photo=photo, bio=bio)
        return redirect('author_list')
    
    return render(request, 'author_create.html')


def author_update_view(request, pk):
    author = get_object_or_404(Author, id=pk)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        bio = request.POST.get('bio')
        photo = request.FILES.get('photo')

        author.full_name = full_name
        author.email = email
        author.bio = bio
        if photo:
            author.photo = photo
        author.save()
        return redirect('author_detail', pk=author.id)
    
    return render(request, 'author_update.html', {'author': author})


def author_delete_view(request, pk):
    author = get_object_or_404(Author, id=pk)

    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    
    return render(request, 'author_delete.html', {'author': author})


def publisher_list_view(request):
    if not get_current_user(request):
        return redirect('login')
    
    publishers = Publisher.objects.all()

    search = request.GET.get('search')
    if search:
        publishers = publishers.filter(name__icontains=search) | publishers.filter(address__icontains=search)

    return render(request, 'publisher_list.html', {'publishers': publishers})


def publisher_detail_view(request, pk):
    publisher = get_object_or_404(Publisher, id=pk)
    return render(request, 'publisher_detail.html', {'publisher': publisher})


def publisher_create_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        logo = request.FILES.get('logo')
        Publisher.objects.create(name=name, address=address, phone=phone, logo=logo)
        return redirect('publisher_list')
    
    return render(request, 'publisher_create.html')


def publisher_update_view(request, pk):
    publisher = get_object_or_404(Publisher, id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        logo = request.FILES.get('logo')

        publisher.name = name
        publisher.address = address
        publisher.phone = phone
        if logo:
            publisher.logo = logo
        publisher.save()
        return redirect('publisher_detail', pk=publisher.id)
    
    return render(request, 'publisher_update.html', {'publisher': publisher})


def publisher_delete_view(request, pk):
    publisher = get_object_or_404(Publisher, id=pk)

    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    
    return render(request, 'publisher_delete.html', {'publisher': publisher})


# def book_list_view(request):
#     books = Book.objects.all()

#     search = request.GET.get('search')
#     if search:
#         books = books.filter(title__icontains=search)

#     min_price = request.GET.get('min_price')
#     max_price = request.GET.get('max_price')

#     if min_price:
#         books = books.filter(price__gt=min_price)
#     if max_price:
#         books = books.filter(price__lt=max_price)

#     return render(request, 'book_list.html', {
#         'books': books,
#         'search': search,
#         'min_price': min_price,
#         'max_price': max_price
#     })


# def book_list_view(request):
#     book_filter = BookFilter(request.GET, queryset=Book.objects.all())
#     return render(request, 'book_list.html', {
#         'books': book_filter.qs,
#         'filter': book_filter,
#     })


def book_list_view(request):
    if not get_current_user(request):
        return redirect('login')
    
    book_filter = BookFilter(
        request.GET,
        queryset=Book.objects.select_related('author', 'category', 'publisher')
    )
    return render(request, 'book_list.html', {
        'books': book_filter.qs,
        'filter': book_filter,
    })


# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     return render(request, 'book_detail.html', {'book': book})


def book_detail_view(request, pk):
    book = get_object_or_404(Book.objects.select_related('author', 'category', 'publisher'), id=pk)
    return render(request, 'book_detail.html', {'book': book})


def book_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        publisher_id = request.POST.get('publisher')
        price = request.POST.get('price')
        pages = request.POST.get('pages')
        description = request.POST.get('description')
        cover = request.FILES.get('cover')
        Book.objects.create(title=title, category_id=category_id, author_id=author_id, publisher_id=publisher_id, price=price, pages=pages, description=description, cover=cover)
        return redirect('book_list')
    
    categories = Category.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'book_create.html', {'categories': categories, 'authors': authors, 'publishers': publishers})


def book_update_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        author_id = request.POST.get('author')
        publisher_id = request.POST.get('publisher')
        price = request.POST.get('price')
        pages = request.POST.get('pages')
        description = request.POST.get('description')
        cover = request.FILES.get('cover')

        book.title = title
        book.category_id = category_id
        book.author_id = author_id
        book.publisher_id = publisher_id
        book.price = price
        book.pages = pages
        book.description = description
        if cover:
            book.cover = cover
        book.save()
        return redirect('book_detail', pk=book.id)
    
    categories = Category.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'book_update.html', {'book': book, 'categories': categories, 'authors': authors, 'publishers': publishers})


def book_delete_view(request, pk):
    book = get_object_or_404(Book, id=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'book_delete.html', {'book': book})


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if username and phone and password:
            UserModel.objects.create(
                username=username,
                phone=phone,
                password=password
            )
            return redirect('login')
        
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        get_user = UserModel.objects.filter(username=username, password=password).first()
        
        if get_user:
            request.session['user_id'] = get_user.id
            return redirect('home')
        
        return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')
    

def forgot_password_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        new_pass = request.POST.get('new_pass')

        get_user = UserModel.objects.filter(phone=phone).first()

        if get_user:
            get_user.password = new_pass
            get_user.save()
            return redirect('login')
        
        return render(request, 'forgot_password.html', {'error': 'No account found with this phone'})

    return render(request, 'forgot_password.html')


def change_password_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')

        get_user = UserModel.objects.filter(
            username=username,
            password=password).first()
        
        if get_user:
            get_user.password = new_password
            get_user.save()
            return redirect('home')
        
    return render(request, 'change_password.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')


def home_view(request):
    get_user = request.session.get('user_id')
    
    if not get_user:
        return redirect('login')
    data = {'data': get_object_or_404(UserModel, id=get_user)}
    return render(request, 'home.html', data)


