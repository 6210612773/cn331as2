from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user.username} "


class Subject(models.Model):
    code = models.CharField(max_length = 5)
    name = models.CharField(max_length = 64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.BooleanField()
    register = models.ManyToManyField(Student, blank = True)
    
    def isfull(self):
        if self.register.count() == self.amount :
            return True

        return False

    def __str__(self):
        return f"{self.code} {self.name}"

class Select_Sub(models.Model) :
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    select = models.ManyToManyField(Subject, blank = True)

    def __str__(self):
        return f"{self.user.username} select {self.select.count()}" 

