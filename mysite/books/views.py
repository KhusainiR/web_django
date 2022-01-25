from django.shortcuts import render
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# relative import of forms
from .models import BooksModel
from .forms import BooksForm

# Create your views here.
def index(request):
    return render(request, "books/home.html")

def home(request):
    context ={}
    context["dataset"] = BooksModel.objects.all()
         
    return render(request, "books/home.html", context)

def create_view(request):
    context ={}
    form = BooksForm(request.POST or None)
    if form.is_valid():

        form.save()
        return HttpResponseRedirect("/home")
         
    context['form']= form
    return render(request, "books/create_view.html", context)

def update_view(request, id):
    context ={}
 
    obj = get_object_or_404(BooksModel, id = id)
 
    form = BooksForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/home")
 
    context["form"] = form
 
    return render(request, "books/update_view.html", context)

def delete_view(request, id):
    context ={}
 
    obj = get_object_or_404(BooksModel, id = id)
 
    form = BooksForm(request.POST or None, instance = obj)

    context["form"] = form

    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/home")
 
    return render(request, "books/delete_view.html", context)