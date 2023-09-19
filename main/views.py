from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
# def show_main(request):
#     products = Product.objects.all()
#     products = [
#         {
#             'title': 'Book of Journeys of Princess Syifa',
#             'author': 'Syifa',
#             'genre': 'Adventure',
#             'price': 100000,
#             'amount': 10,
#             'synopsis': 'This is a story about a princess named Syifa who likes to travel around the world.',
#         },
#         {
#             'title': 'Kayza and Azmy: a Love Story',
#             'author': 'Syifa',
#             'genre': 'Romance',
#             'price': 20000,
#             'amount': 20,
#             'synopsis': 'A book about a love story between Kayza and Azmy. They are a couple who have been together for 5 years.',
#         },
#         {
#             'title': 'Anisha Fashion Frenzy',
#             'author': 'Syifa',
#             'genre': 'Fashion',
#             'price': 30000,
#             'amount': 30,
#             'synopsis': 'A book about fashion by Anisha. This book is suitable for those of you who like fashion.',
#         },
#         {
#             'title': 'Healthy Productivity: by Shafira',
#             'author': 'Syifa',
#             'genre': 'Productivity',
#             'price': 40000,
#             'amount': 40,
#             'synopsis': 'A book about productivity by Shafira. This book is suitable for those of you who want to be productive.',
#         },
#         {
#             'title': 'Farah Squishy Castle',
#             'author': 'Syifa',
#             'genre': 'Children',
#             'price': 50000,
#             'amount': 50,
#             'synopsis': 'This book tells the story of Farah and her castle that made of squishies',
#         }
#     ]

#     context = {
#         'products': products,
#     }
    
#     return render(request, "main.html", context)


def show_main(request):
   
    products = Product.objects.all()
    
    context = {
        'products': products,
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

