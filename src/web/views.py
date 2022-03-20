from django.shortcuts import render
from tcore.models import TempLog

def temp_view(request):
    return render(request, 'index.html')

# Create your views here.
