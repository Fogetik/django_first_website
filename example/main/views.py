from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'main/mainPage.html', {'title':'Главная', 'blogs':blogs})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верная'

    form = BlogForm()
    context = {
        'form': form,
        'error' : error
    }
    return render(request, 'main/create.html', context)

