# Generated by Django 3.2.7 on 2021-09-14 13:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0002_auto_20210914_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='register',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
