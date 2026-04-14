from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Publisher, Book


def category_list_view(request):
    categories = Category.objects.all()

    # Поиск по имени и описанию
    q = request.GET.get('q')
    desc = request.GET.get('desc')
    if q:
        categories = categories.filter(name__icontains=q)
    if desc:
        categories = categories.filter(description__icontains=desc)

    return render(request, 'category_list.html', {'categories': categories})


def home_view(request):
    return render(request, 'home.html')


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


def author_list_view(request):
    authors = Author.objects.all()

    search = request.GET.get('search')
    if search:
        authors = authors.filter(
            full_name__icontains=search
        ) | authors.filter(
            email__icontains=search
        )

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
    publishers = Publisher.objects.all()

    search = request.GET.get('search')
    if search:
        publishers = publishers.filter(
            name__icontains=search
        ) | publishers.filter(
            address__icontains=search
        )

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


def book_list_view(request):
    books = Book.objects.all()

    search = request.GET.get('search')
    if search:
        books = books.filter(
            title__icontains=search
        ) | books.filter(
            author__full_name__icontains=search
        )

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_pages = request.GET.get('min_pages')
    max_pages = request.GET.get('max_pages')

    if min_price:
        books = books.filter(price__gte=min_price)
    if max_price:
        books = books.filter(price__lte=max_price)
    if min_pages:
        books = books.filter(pages__gte=min_pages)
    if max_pages:
        books = books.filter(pages__lte=max_pages)

    return render(request, 'book_list.html', {
        'books': books,
        'search': search,
        'min_price': min_price,
        'max_price': max_price,
        'min_pages': min_pages,
        'max_pages': max_pages,
    })


def book_detail_view(request, pk):
    book = get_object_or_404(Book, id=pk)
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