import json

from django.http import HttpResponse
from django.views import View
from httpx import Client
import logging
import requests
import random

from ..models import Video, ExternalApi
from ..serializers import VideoSerializer

logger = logging.getLogger(__name__)


class VideoView(View):

    def __init__(self):
        self.client = Client()
        self.model = Video
        self.serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
        last_frame = request.GET.get('last_frame', None)
        external_path = ExternalApi.objects.filter(name='FrameX').values_list('url', flat=True)[0]
        video_data = json.loads(requests.get(external_path).text)[0]
        url = video_data['url']
        frame = None
        if last_frame:
            num = last_frame + 50
            next_frame = f'frame/{str(num)}/'  ##Provisional
            frame = url.join(f'frame/{next_frame}/')
        else:
            num = random.randrange(1, video_data["frames"], 5)
            rand_frame = f'frame/{str(num)}/'
            frame = url + rand_frame
        return HttpResponse(frame)
