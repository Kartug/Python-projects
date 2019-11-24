from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from products.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from products.forms import ProductCreate
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = Product
    template_name = 'products/home.html'
#     allProds = []
#     catprods = Product.objects.values('category')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)

#     params = {'allProds': allProds}


# def Home(request, category_slug=None):
#     model = Product
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(category)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=category)

#     context = {
#         'category': category,
#         'categories': categories,
#         'products': products
#     }
#     return render(request, 'products/home.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.values('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'products/product_detail', context)


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'


# def index(request):
#     shelf = Product.objects.all()
#     return render(request, 'products/admin.html', {'shelf': shelf})


def upload(request):

    upload = ProductCreate()
    if request.method == 'POST':
        upload = ProductCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'products:home'}}">reload</a>""")
    else:
        return render(request, 'products/upload_form.html', {'upload_form': upload})


def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('home')
    product_form = ProductCreate(request.POST or None, instance=product_sel)
    if product_form.is_valid():
        product_form.save()
        return redirect('home')
    return render(request, 'products/upload_form.html', {'upload_form': product_form})


def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('home')
    product_sel.delete()
    return redirect('home')
