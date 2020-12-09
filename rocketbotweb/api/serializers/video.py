from rest_framework import serializers
from ..models import video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ('name', 'width', 'height', 'frames', 'frame_rate', 'url', 'first_frame', 'last_frame')
