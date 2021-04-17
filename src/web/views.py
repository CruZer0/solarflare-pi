from django.shortcuts import render
from tcore.models import TempLog

def temp_view(request):
    db = TempLog.objects.get(id=2)
    context = {
        'db' : db,
    }
    return render(request, 'index.html', context)

# Create your views here.
