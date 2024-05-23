from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    context = {
        'title': 'Home - Main Page',
        'content': 'The Glade',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - About Us Page',
        'content': 'The Glade',
        'text_on_page': "Welcome to The Glade, where style meets urban culture. We curate the latest trends and timeless classics to bring you a unique selection of clothing and accessories that reflect the spirit of the modern city dweller. From streetwear staples to high-end fashion, our collection embodies the vibrant energy and diversity of urban life. Step into our emporium and discover a world of fashion-forward designs, quality craftsmanship, and effortless cool. Join the Urban Era movement today."
    }
    return render(request, 'main/about.html', context)


def contact(request):
    context = {
        'title': 'Home - Contact Us Page',
        'content': 'Contact The Glade',
        'text_on_page': (
            "Contact Information:\n"
            "Email 1: nazaruk7649@ukr.net\n"
            "\n"
            "Email 2: ivan001nazaruk@gmail.com\n"
            "\n"
            "Address: West London\n"
            "\n"
            "Feel free to reach out for any information or inquiries."
        ),
    }
    return render(request, 'main/contact.html', context)


def ship_payment(request):
    context = {
        'title': 'Home - Shipping and Payment Information',
        'content': 'The Glade',
        'text_on_page': (
            "Shipping and Payment Information:\n"
            "\n"
            ">>>We have our own delivery service that guarantees 100% safe delivery. You can trust that your purchases will arrive on time and in perfect condition. For payment, we offer a variety of options to suit your needs, ensuring a smooth and hassle-free shopping experience.\n"
            "\n"
            ">>>Contact us for any information and inquiries."
        ),
    }
    return render(request, 'main/ship_payment.html', context)



