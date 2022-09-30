from django.shortcuts import render, get_object_or_404

# Create your views here.
def products(request):
    
    return render(request, 'products/products.html')


