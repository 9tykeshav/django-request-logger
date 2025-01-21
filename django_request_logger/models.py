from django.db import models


class RequestLog(models.Model):
    url_name = models.CharField(max_length=255)
    timestamp = models.BigIntegerField()
    path = models.CharField(max_length=255)
    response_code = models.IntegerField()
    processing_time = models.IntegerField()
    method = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.method} {self.path} - {self.response_code}"
