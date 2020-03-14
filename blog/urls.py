from django.urls import path,re_path
from .views import *

urlpatterns=[
	path('<int:postid>/',BlogDetailsView.as_view()),
	path('like/',BlogLikeView.as_view()),
	path('comment/',BlogCommentView.as_view()),
	path('',BlogView.as_view()),
]