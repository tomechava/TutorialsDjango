from django.urls import path, include
from .views  import homePageView

urlPatterns = [
    path("", homePageView, name='home'),
    path('', include('pages.urls')),
]