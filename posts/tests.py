from django.test import TestCase
from .models import *

# Create your tests here.
class PostModelTest(Post):
    def setUp(self):
        post=Post.objects.get(text='second post')
    def test_post_model(self):
        post=Post.objects.get(id=2)
        text='second post'
        self.assertEqual(text, f"{post.text}")