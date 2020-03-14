from django.urls import path,re_path
from .views import *


urlpatterns=[
	path('',GalleryView.as_view()),
]