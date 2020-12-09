from django.db import models


class ExternalApi(models.Model):

    name = models.CharField(max_length=50, blank=False)
    url = models.CharField(max_length=155)

    def __str__(self):
        return self.name
