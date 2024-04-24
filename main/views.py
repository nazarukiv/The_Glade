from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Main Page',
        'content': 'Urban Era Emporium',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - About Us Page',
        'content': 'Urban Era Emporium',
        'text_on_page': "Welcome to Urban Era Emporium, where style meets urban culture. We curate the latest trends and timeless classics to bring you a unique selection of clothing and accessories that reflect the spirit of the modern city dweller. From streetwear staples to high-end fashion, our collection embodies the vibrant energy and diversity of urban life. Step into our emporium and discover a world of fashion-forward designs, quality craftsmanship, and effortless cool. Join the Urban Era movement today."
    }
    return render(request, 'main/about.html', context)


