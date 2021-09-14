from django.contrib import admin

# Register your models here.

from .models import Subject, Student , Select_Sub

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "semester", "year", "seat", "status")
class Select_SubAdmin(admin.ModelAdmin):
    filter_horizontal = ("select",)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student)
admin.site.register(Select_Sub, Select_SubAdmin)
