from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django import forms


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "About us - Online Store",
                "subtitle": "About us",
                "description": "This is an about page ...",
                "author": "Developed by: Your Name",
            }
        )
        return context


class ContactPageView(TemplateView):
    template_name = "pages/contact.html"


class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 2000},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 1000},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 50},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 20},
    ]


class ProductIndexView(View):
    template_name = "products/index.html"

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = "products/show.html"

    def get(self, request, id):
        viewData = {}
        if(int(id) - 1 > len(Product.products) and int(id) >= 0):
            return HttpResponseRedirect("/")
        
        product = Product.products[int(id) - 1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        
        return render(request, self.template_name, viewData)
        
        
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True, min_value=0)
 
class ProductCreateView(View):
    template_name = 'products/create.html'
 
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():

            return redirect("success")
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)

class SuccessPageView(TemplateView):
    template_name = "products/success.html"
    
        
