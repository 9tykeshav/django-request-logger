from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.urls import resolve
import time
from .models import RequestLog


class RequestLogger:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.DJANGO_REQUEST_LOGGER_DATABASE: str = getattr(
            settings, "DJANGO_REQUEST_LOGGER_DATABASE", "default"
        )

    def __call__(self, request: HttpRequest) -> HttpResponse:
        normalized_path = request.path
        view_url_name = resolve(normalized_path).url_name

        request_data = {
            "timestamp": int(time.time() * 1000),  # Convert to milliseconds
            "path": normalized_path,
            "method": request.method,
            "url_name": view_url_name,
        }

        resp: HttpResponse = self.get_response(request)

        RequestLog.objects.create(
            url_name=request_data["url_name"],
            timestamp=request_data["timestamp"],
            path=request_data["path"],
            response_code=resp.status_code,
            processing_time=int(time.time() * 1000)
            - request_data["timestamp"],  # Convert to milliseconds
            method=request_data["method"],
        )

        return resp
