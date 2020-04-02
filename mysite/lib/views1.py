# lib/views.py
from django.shortcuts import render
from lib.models import Book
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def updateBook(request,book_id):
    bookID = book_id
    book_list=Book.objects.filter(id=bookID)
    context = {'book_list': book_list}
    return render(request, 'lib/detail_update.html', context)
    # return HttpResponse("Hello, world!qlq"+str(book_id))

def index(request):
    return render(request, 'lib/index.html')