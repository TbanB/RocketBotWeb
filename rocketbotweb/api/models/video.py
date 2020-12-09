from django.db import models


class Video(models.Model):

    name = models.CharField(max_length=50, blank=False)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    frames = models.IntegerField(default=0)
    frame_rate = models.CharField(max_length=155, blank=True)
    url = models.CharField(max_length=155)
    first_frame = models.CharField(max_length=155, blank=True)
    last_frame = models.CharField(max_length=155, blank=True)

    def __str__(self):
        return self.name
