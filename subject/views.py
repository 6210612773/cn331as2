from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *

def index(request):
    index = Subject.objects.all()

    return render(request, "subject/index.html", {"subject":index})