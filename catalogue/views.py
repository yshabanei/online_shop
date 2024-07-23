from django.db.models import Q
from django.http import HttpResponse
from catalogue.models import Product, Category, ProductType, Brand


def product_list(request):
    # products = Product.objects.filter(is_active=True)
    # products = Product.objects.exclude(is_active=False)
    # category = Category.objects.first()
    # category = Category.objects.last()
    # category = Category.objects.get(id=1)
    # products = Product.objects.filter(is_active=True, category=category)
    # category = Category.objects.filter(name="Book").first()
    # products = Product.objects.filter(is_active=True, category__name="Book")
    # product_type = ProductType.objects.filter(title="Book")
    # brand = Brand.objects.first()
    # new_product = Product.objects.create(
    #     product_type=product_type,
    #     upc=741852,
    #     title="Test Product",
    #     description="",
    #     category=Category,
    #     brand=brand,
    # )

    products = Product.objects.select_related("category").all()
    context = "\n".join(
        [
            f"{product.title}, {product.upc}, {product.category.name}"
            for product in products
        ]
    )
    return HttpResponse(context)


def product_detail(request, pk):
    # try:
    #     product = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     return HttpResponse("Product does not exist")
    product = Product.objects.filter(is_active=True).filter(Q(pk=pk) | Q(upc=pk))
    if product.exists():
        product = product.first()
        return HttpResponse(f"title:{product.title}")
    return HttpResponse("Product does not exist")


def category_products(request, pk):
    try:
        category = Category.objects.prefetch_related("products").get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category does not exist")
    products = category.products.all()
    product_ids = [1, 2, 3]
    products = Product.objects.filter(id__in=product_ids)
    # products = Product.objects.filter(category=category)

    context = "\n".join([f"{product.title}, {product.upc}" for product in products])
    return HttpResponse(context)
