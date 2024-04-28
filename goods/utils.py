from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:             #for search by id
        return Products.objects.filter(id=int(query))

