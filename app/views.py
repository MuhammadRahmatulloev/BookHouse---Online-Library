from django.shortcuts import render, get_object_or_404, redirect
from .models import Category


def category_list_view(request):
    category = {'category': Category.objects.all()}
    return render(request, 'category_list.html', category)


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

        return redirect('detail', pk=category.id)

    return render(request, 'category_update.html', {'category': category})


def category_delete_view(request, pk):
    category = get_object_or_404(Category, id=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('list')

    return render(request, 'category_delete.html', {'category': category})

