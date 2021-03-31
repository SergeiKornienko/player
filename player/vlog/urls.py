from . import views
from django.urls import path

urlpatterns = [
    path('', views.VideosView.as_view()),
    path('<int:pk>/', views.VideoDetailView.as_view(), name='video_detail')
]
