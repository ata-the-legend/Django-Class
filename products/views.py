from django.shortcuts import render, HttpResponse
from .models import Category, Product, ProductPrice

# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:10]
    category_response = ''
    for c in categories:
        category_response += f'<li><a href="/categories/{c.id}/{c.slug}">{c.name}</a></li>' 
    category_response = f'<ul>{category_response}</ul>'

    product_response = ''
    for p in products:
        product_response += f'<li><a href="/products/{p.id}">{p.name}</a></li>'
    product_response = f"<ul>{product_response}</ul>"

    return HttpResponse(f"""
                        <html>
                        <head><title>Digikala</title></head>
                        <body>
                        <h1>the best seller site in iran</h1>
                        <h3>Categories</h3>
                        {category_response}
                        <h3>Products</h3>
                        {product_response}
                        </body>
                        </html>
                        """)
    # return HttpResponse('<Ali>')
    # print(categories, products)

def product_view(request, product_id):
    try:
        p = Product.objects.get(id=product_id)
        # price = ProductPrice.objects.get(product=product_id)
        price = ProductPrice.objects.filter(product=product_id)
        return HttpResponse(f"""
                        <html>
                        <head><title>Digikala</title></head>
                        <body>
                        <h1>{p.name}</h1>
                        <h2>{p.en_name}</h2>
                        <h5>{p.category}</h5>
                        <h4>{price[0]}</h4>
                        <p>{p.description}</p>
                        </body>
                        </html>
                        """)
    except Product.DoesNotExist:
        return HttpResponse('404 Product not found')



def category_view(request, category_slug, category_id):
    try:
        # c = Category.objects.get(id=category_id)
        c = Category.objects.get(slug=category_slug)
        return HttpResponse(f"""
                            <html>
                            <head><title>Digikala</title></head>
                            <body>
                            <h1>{c.name}</h1>
                            <h5>{c.parent}</h5>
                            <p>{c.description}</p>
                            </body>
                            </html>
                            """)
    except Category.DoesNotExist:
        return HttpResponse('404 Category not found')
    