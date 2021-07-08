from .views import HomePageView
from django.urls.conf import path
from .models import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home' )
]
