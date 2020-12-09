from django.urls import path

from .views import BotView, VideoView

urlpatterns = [
    path('video/', VideoView.as_view(), name='video-view'),
    path('bot/', BotView.as_view(), name='bot-view'),
]
