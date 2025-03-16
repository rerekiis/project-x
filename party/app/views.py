from django.shortcuts import render
from .models import Party
# Create your views here.

def index(request):
    return render(request, 'index.html')

