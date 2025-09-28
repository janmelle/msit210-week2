from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'home',
        'features': ['Django', 'Templates', 'Static', 'Models', 'ORM', 'CRUD'],
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'about'})

def hello(request, name):
    return render(request, 'hello.html', {'name': name, 'title': 'hello'})