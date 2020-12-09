from django.urls import path

from .views.video import VideoView

urlpatterns = [
    path('video/', VideoView.as_view(), name='video-view'),
]
