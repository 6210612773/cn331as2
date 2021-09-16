# Generated by Django 3.2.6 on 2021-09-15 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subject', '0004_alter_subject_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='isfull',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='register',
            field=models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]