from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from categories.forms import CategoryCreateForm, CategoryEditForm, CategoryDeleteForm
from categories.models import Category


def categories_list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'categories/categories_list.html', context)

def create_category(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryCreateForm()

    context = {
        'form': form
    }

    return render(request, 'categories/create_category.html', context)

def category_details(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category
    }

    return render(request, 'categories/category_details.html', context)

def edit_category(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryEditForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_details', pk=pk)
    else:
        form = CategoryEditForm(instance=category)

    context = {
        'category': category,
        'form': form
    }

    return render(request, 'categories/edit_category.html', context)

def delete_category(request: HttpRequest, pk: int) -> HttpResponse:
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories_list')

    form = CategoryDeleteForm(instance=category)

    context = {
        'category': category,
        'form': form
    }

    return render(request, 'categories/delete_category.html', context)