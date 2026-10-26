from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from publishers.forms import PublisherCreateForm, PublisherEditForm, PublisherDeleteForm
from publishers.models import Publisher


def publishers_list (request: HttpRequest) -> HttpResponse:
    publishers = Publisher.objects.all()
    context = {
        'publishers': publishers
    }

    return render(request, 'publishers/publishers_list.html', context)

def create_publisher(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PublisherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publishers_list')
    else:
        form = PublisherCreateForm()

    context = {
        'form': form
    }

    return render(request, 'publishers/create_publisher.html', context)

def publisher_details(request: HttpRequest, pk: int) -> HttpResponse:
    publisher = get_object_or_404(Publisher, pk=pk)
    context = {
        'publisher': publisher
    }

    return render(request, 'publishers/publisher_details.html', context)

def edit_publisher(request: HttpRequest, pk: int) -> HttpResponse:
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        form = PublisherEditForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_details', pk=pk)
    else:
        form = PublisherEditForm(instance=publisher)

    context = {
        'publisher': publisher,
        'form': form
    }

    return render(request, 'publishers/edit_publisher.html', context)

def delete_publisher(request: HttpRequest, pk: int) -> HttpResponse:
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publishers_list')

    form = (PublisherDeleteForm
            (instance=publisher))
    context = {
        'publisher': publisher,
        'form': form
    }

    return render(request, 'publishers/delete_publisher.html', context)

