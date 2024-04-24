from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': [
    {
        'image': 'deps/images/goods/supreme_logo.png',
        'name': 'Supreme Logo T-shirt',
        'description': 'Description of Supreme Logo T-shirt',
        'price': 150.00
    },
    {
        'image': 'deps/images/goods/off.png',
        'name': 'Big Bookish Skate Tee Off-White',
        'description': 'Part of Wardrobe, the curated selection of Off-White™ staples, this crewneck t-shirt features oversized branding and has a relaxed skate fit. 100% cotton.',
        'price': 200.00
    },
    {
        'image': 'deps/images/goods/jacket_carhartt.jpeg',
        'name': 'Carhartt Jacket',
        'description': 'Description of Carhartt Jacket',
        'price': 110.00
    },
    {
        'image': 'deps/images/goods/patagonia_bag.png',
        'name': 'Patagonia Bag',
        'description': 'Description of Patagonia Bag',
        'price': 35.00
    },
    {
        'image': 'deps/images/goods/tracksuit.png',
        'name': 'Tracksuit Corteiz',
        'description': 'Description of Tracksuit Corteiz',
        'price': 160.00
    },
    {
        'image': 'deps/images/goods/bape_t_shirt.png',
        'name': 'T-shirt Bape',
        'description': 'Description of T-shirt Bape',
        'price': 60.00
    },
    {
        'image': 'deps/images/goods/nike_ring.png',
        'name': 'Nike Ring',
        'description': 'Description of Nike Ring',
        'price': 20.00
    },
    {
        'image': 'deps/images/goods/stussy_t_shirt.png',
        'name': 'T-shirt Stussy',
        'description': 'Description of T-shirt Stussy',
        'price': 50.00
    },
    {
        'image': 'deps/images/goods/essential_hoodie.png',
        'name': 'Hoodie Fear of God , Essential',
        'description': 'Description of Hoodie Fear of God , Essential',
        'price': 75.00
    },
    {
        'image': 'deps/images/goods/windbreaker_corteiz.png',
        'name': 'Corteiz Windbreaker',
        'description': 'Description of Corteiz Windbreaker',
        'price': 90.00
    },
    {
        'image': 'deps/images/goods/adidas_samba.png',
        'name': 'Adidas Samba Sneakers',
        'description': 'Description of Adidas Samba Sneakers',
        'price': 62.00
    },
    {
        'image': 'deps/images/goods/new_balance_shoese.png',
        'name': 'New Balance Sneakers',
        'description': 'Description of New Balance Sneakers',
        'price': 120.00
    }
]
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')
