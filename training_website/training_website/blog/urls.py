from django.urls import path
from .views import *

url_patterns = [
    path('', index, name='index'),
    path(r'^blog/<int: post_id>/', post, name='post'),
]