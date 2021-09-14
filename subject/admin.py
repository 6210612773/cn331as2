from django.contrib import admin

# Register your models here.

from .models import Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "semester", "year", "seat", "status")


admin.site.register(Subject, SubjectAdmin)


