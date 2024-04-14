from django.shortcuts import render
from django.core.paginator import Paginator

from .utils import get_mongodb
def main(request, page = 1):
    db = get_mongodb()
    quotes = db.quotes.find()
    par_page = 10
    paginator = Paginator(list(quotes), par_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
     

def Austen(request):
    return render(request, 'quotes\Austen.html')

def Einstein(request):
    return render(request, 'quotes\Einstein.html')

def Rowling(request):
    return render(request, 'quotes\Rowling.html')

def Gide(request):
    return render(request, 'quotes\Gide.html')

def Monroe(request):
    return render(request, 'quotes\Monroe.html')

def Edison(request):
    return render(request, 'quotes\Edison.html')

def Roosevelt(request):
    return render(request, 'quotes\Roosevelt.html')

def Martin(request):
    return render(request, 'quotes\Martin.html')