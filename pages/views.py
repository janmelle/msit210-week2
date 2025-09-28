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

def gallery(request):
    images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
    return render(request, 'gallery.html', {'title': 'gallery', 'images': images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)