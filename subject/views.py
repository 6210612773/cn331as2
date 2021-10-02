from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import *

def index(request):
    index = Subject.objects.all()

    return render(request, "subject/index.html", {"subject":index})

def subjectPage(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    return render(request, "subject/subject.html", {
        "subject": subject,
        "students": subject.register.all(),
    })

def register(request, subject_id):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))

    subject = get_object_or_404(Subject, pk=subject_id)
    if request.user not in subject.register.all():
        subject.register.add(request.user)
        select = Subject.objects.get(id=subject_id)
        select.count += 1
        if select.count == select.seat:
            select.isfull = True
        if select.count < select.seat:
            select.isfull = False
        select.save()
    return HttpResponseRedirect(reverse("subject:subject", args=(subject_id,)))


def remove(request, subject_id):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))

    subject = get_object_or_404(Subject, pk=subject_id)
    if request.user in subject.register.all():
        subject.register.remove(request.user)
        select = Subject.objects.get(id=subject_id)
        select.count -= 1
        if select.count < select.seat:
            select.isfull = False
        select.save()
    return HttpResponseRedirect(reverse("subject:subject", args=(subject_id,)))