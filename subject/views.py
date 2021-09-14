from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *

def index(request):
    index = Subject.objects.all()

    return render(request, "subject/index.html", {"subject":index})

def subjectPage(request, subject_id):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))
    subject = Subject.objects.get(pk=subject_id)
    return render(request, "subject/subject.html", {
        "subject": subject
    })