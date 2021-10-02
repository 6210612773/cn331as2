from django.http import request
from django.shortcuts import get_object_or_404
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from subject.models import Subject
password = make_password('1234')

# Create your tests here.

class SubjectModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='user1', password = password, email='user1@example.com')
        subject = Subject.objects.create(code='cn122', name='sub1', seat = '2', semester = '1', year = '2020' ,status='False')
        subject2 = Subject.objects.create(code='cn123', name='sub2', seat = '1', semester = '1', year = '2020' ,status='True')

    def test_index_view_with_authentication(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('subject:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_subject(self):
        c = Client()
        s1 = Subject.objects.first()
        s1.save()
        response = c.get(reverse('subject:subject', args=(s1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_register_without_authentication(self):
        s1 = Subject.objects.first()
        s1.save()

        c = Client()
        response = c.get(reverse('subject:register', args=(s1.id,)))
        self.assertEqual(s1.register.count(), 0)

    def test_register_with_authentication(self):
        user = User.objects.get(username='user1')
        s1 = Subject.objects.first()
        s1.save()

        c = Client()
        c.force_login(user)
        response = c.get(reverse('subject:register', args=(s1.id,)))
        self.assertEqual(s1.register.count(), 1)

    def test_remove_without_authentication(self):
        s1 = Subject.objects.first()
        s1.save()

        c = Client()
        response = c.get(reverse('subject:remove', args=(s1.id,)))
        self.assertEqual(s1.register.count(), 0)

    def test_remove_with_authentication(self):
        user = User.objects.get(username='user1')
        s1 = Subject.objects.first()
        s1.save()

        c = Client()
        c.force_login(user)
        response1 = c.get(reverse('subject:register', args=(s1.id,)))
        self.assertEqual(s1.register.count(), 1)
        response2 = c.get(reverse('subject:remove', args=(s1.id,)))
        self.assertEqual(s1.register.count(), 0)

    def test_register_subject_full(self):
        user = User.objects.get(username='user1')        
        c = Client()
        s2 = Subject.objects.get(id=2)
        s2.save()
        c = Client()
        c.force_login(user)
        response = c.get(reverse('subject:register', args=(s2.id,)))
        self.assertEqual(s2.register.count(), 1)

    def test_remove_subject_not_full(self):
        user = User.objects.get(username='user1')
        s2 = Subject.objects.get(id = 2)
        s2.save()

        c = Client()
        c.force_login(user)
        response1 = c.get(reverse('subject:register', args=(s2.id,)))
        self.assertEqual(s2.register.count(), 1)
        response2 = c.get(reverse('subject:remove', args=(s2.id,)))
        self.assertEqual(s2.register.count(), 0)

