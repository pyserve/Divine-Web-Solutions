from django.urls import path,re_path
from .views import *

urlpatterns=[
	path('',HomeView.as_view()),
	path('home/',HomeView.as_view(),name='home'),
	path('accounts/login/',LoginView.as_view(),name='login'),
	path('accounts/register/',RegisterView.as_view()),
	path('accounts/logout/',LogoutView.as_view(),name='logout'),
	path('accounts/verify/<int:uid>/<str:verify_id>/',AccountVerifyView.as_view(),name='verify')
]