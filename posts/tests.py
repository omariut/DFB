from django.test import TestCase
from .models import *
from django.urls import reverse

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        post=Post.objects.create(text='second post')
    def test_post_model(self):
        post=Post.objects.get(id=1)
        text='second post'
        self.assertEqual(f"{post.text}",text)


class HomePageViewTest(TestCase):
    def test_view_url_exist_proper_location(self):
        res=self.client.get(reverse('home'))
        self.assertEqual(res.status_code,200)
    def test_correct_template(self):
        res=self.client.get(reverse('home'))
        self.assertTemplateUsed(res, 'home.html')
