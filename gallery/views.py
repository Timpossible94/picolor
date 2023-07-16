from django.shortcuts import render
from . models import *
# Create your views here.

def home(request):
    return render(request, 'gallery/home.html')

def gallery(request):
    bilder = Bild.objects.all()
    ctx = {'bilder':bilder}
    return render(request, 'gallery/gallery.html', ctx)

def contact(request):
    return render(request, 'gallery/contact.html')
    
    