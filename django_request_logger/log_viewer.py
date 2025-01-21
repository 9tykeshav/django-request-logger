"""
This module provides a viewer for request logs, including various methods to analyze and visualize the logs.

Classes:
    RequestLogsViewer: A class to view and analyze request logs.
"""

from django.conf import settings
from typing import List, Optional
from collections import defaultdict
from datetime import datetime

from django_request_logger.types import (
    EndpointUsageData,
    ErrorResponsesData,
    HttpMethodData,
    ResponseCodeData,
    RequestOverTimeData,
)
from .models import RequestLog
import matplotlib.pyplot as plt


class RequestLogsViewer:
    """
    A class to view and analyze request logs.

    Methods:
        print_logs: Prints all request logs.
        endpoint_usage: Analyzes endpoint usage.
        resp_code_distribution: Analyzes response code distribution.
        error_responses: Analyzes error responses.
        http_method_distribution: Analyzes HTTP method distribution.
        single_endpoint_http_method: Analyzes HTTP method distribution for a single endpoint.
        requests_over_time: Analyzes the number of requests over time.
    """

    def __init__(self) -> None:
        self.db = getattr(settings, "DJANGO_REQUEST_LOGGER_DATABASE", "default")

    def print_logs(self):
        """
        Prints all request logs.
        """
        logs = RequestLog.objects.all()

    def endpoint_usage(self, exclude: Optional[List[str]] = []):
        """
        Analyzes endpoint usage.

        Args:
            exclude (Optional[List[str]]): A list of endpoints to exclude from the analysis.

        Returns:
            EndpointUsageData: An object containing the endpoint usage data.
        """
        logs = RequestLog.objects.all().exclude(url_name__in=exclude)
        piechart_data = {}
        for log in logs:
            if log.url_name not in piechart_data.keys():
                piechart_data[log.url_name] = 1
            piechart_data[log.url_name] += 1

        return EndpointUsageData(piechart_data)

    def resp_code_distribution(
        self, url_name: Optional[str] = None, exclude: Optional[List[str]] = []
    ):
        """
        Analyzes response code distribution.

        Args:
            url_name (Optional[str]): The URL name to filter the logs.
            exclude (Optional[List[str]]): A list of endpoints to exclude from the analysis.

        Returns:
            ResponseCodeData: An object containing the response code distribution data.
        """
        if url_name:
            logs = RequestLog.objects.all().filter(url_name=url_name)
        else:
            logs = RequestLog.objects.all().exclude(url_name__in=exclude)
        piechart_data = {}
        for log in logs:
            if log.response_code not in piechart_data.keys():
                piechart_data[log.response_code] = 1
            piechart_data[log.response_code] += 1

        return ResponseCodeData(piechart_data, url_name)

    def error_responses(self, exclude: Optional[List[str]] = []):
        """
        Analyzes error responses.

        Args:
            exclude (Optional[List[str]]): A list of endpoints to exclude from the analysis.

        Returns:
            ErrorResponsesData: An object containing the error response data.
        """
        logs = RequestLog.objects.all().exclude(url_name__in=exclude)
        error_data = {}
        for log in logs:
            if not (200 <= log.response_code < 300):
                if log.url_name not in error_data.keys():
                    error_data[log.url_name] = 1
                else:
                    error_data[log.url_name] += 1

        return ErrorResponsesData(error_data)

    def http_method_distribution(self, exclude: Optional[List[str]] = []):
        """
        Analyzes HTTP method distribution.

        Args:
            exclude (Optional[List[str]]): A list of endpoints to exclude from the analysis.

        Returns:
            HttpMethodData: An object containing the HTTP method distribution data.
        """
        logs = RequestLog.objects.all().exclude(url_name__in=exclude)
        method_data = {}
        for log in logs:
            if log.method not in method_data.keys():
                method_data[log.method] = 1
            else:
                method_data[log.method] += 1

        return HttpMethodData(method_data)

    def single_endpoint_http_method(self, url_name: str):
        """
        Analyzes HTTP method distribution for a single endpoint.

        Args:
            url_name (str): The URL name to filter the logs.

        Returns:
            HttpMethodData: An object containing the HTTP method distribution data for the specified endpoint.
        """
        logs = logs = RequestLog.objects.all().filter(url_name=url_name)
        method_data = {}
        for log in logs:
            if log.method not in method_data.keys():
                method_data[log.method] = 1
            else:
                method_data[log.method] += 1

        return HttpMethodData(method_data, url_name=url_name)

    def requests_over_time(
        self, interval: str = "daily", exclude: Optional[List[str]] = []
    ):
        """
        Analyzes the number of requests over time.

        Args:
            interval (str): The time interval for the analysis ('daily', 'weekly', or 'monthly').
            exclude (Optional[List[str]]): A list of endpoints to exclude from the analysis.

        Returns:
            RequestOverTimeData: An object containing the request data over time.
        """
        logs = RequestLog.objects.all().exclude(url_name__in=exclude)
        time_data = defaultdict(int)

        for log in logs:
            timestamp = datetime.fromtimestamp(log.timestamp / 1000)
            if interval == "daily":
                time_key = timestamp.date()
            elif interval == "weekly":
                time_key = timestamp.strftime("%Y-%U")  # Year-WeekNumber
            elif interval == "monthly":
                time_key = timestamp.strftime("%Y-%m")  # Year-Month
            else:
                raise ValueError(
                    "Invalid interval. Choose from 'daily', 'weekly', or 'monthly'."
                )

            time_data[time_key] += 1
        print(time_data)
        return RequestOverTimeData(dict(time_data), interval)
