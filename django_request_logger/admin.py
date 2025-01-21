from django.contrib import admin

from .models import RequestLog


@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = (
        "url_name",
        "timestamp",
        "path",
        "response_code",
        "processing_time",
        "method",
    )
    search_fields = ("url_name", "path", "method")
    list_filter = ("response_code", "method")
