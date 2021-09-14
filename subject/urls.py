from django.urls import path

from . import views
app_name="subject"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:subject_id>', views.subjectPage, name="subject"),
    path('<int:subject_id>/register', views.register, name="register"),
    path('<int:subject_id>/remove', views.remove, name="remove"), 
]   