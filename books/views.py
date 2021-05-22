from django import http
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BooksModel
from.forms import BooksForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def add(request):
    return render(request,'books/add.html')

def listing(request):
    data = BooksModel.objects.all()
    return render(request,"books/listing.html",{"data":data})


def add_model(request):
    if request.POST:
            form = BooksForm(request.POST,request.FILES)
            if form.is_valid():
                books = BooksModel()
                books.name = form.cleaned_data["name"]
                books.author = form.cleaned_data["author"]
                books.price = form.cleaned_data["price"]
                books.img = form.cleaned_data["img"]
                # form.save()
                books.save()
                return redirect('/books/listing/')
            else:
                return redirect('/books/add/')
    else:
        return HttpResponse("Wrong")