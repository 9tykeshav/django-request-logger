"""
This module defines various data classes for logging and visualizing request data.

Classes:
    RequestLog: A placeholder class for request logs.
    EndpointUsageData: Handles data and visualization for endpoint usage.
    ResponseCodeData: Handles data and visualization for response code distribution.
    ErrorResponsesData: Handles data and visualization for error responses.
    HttpMethodData: Handles data and visualization for HTTP method distribution.
    RequestOverTimeData: Handles data and visualization for requests over time.
"""

from typing import Optional
from matplotlib import pyplot as plt, colormaps


class RequestLog:
    """
    A placeholder class for request logs.
    """

    def __init__(self) -> None:
        pass


class EndpointUsageData:
    """
    Handles data and visualization for endpoint usage.

    Attributes:
        data (dict): A dictionary containing endpoint usage data.
    """

    def __init__(self, data: dict):
        self.data = data

    def piechart(self):
        """
        Generates a pie chart for endpoint usage distribution.

        Returns:
            tuple: A tuple containing the figure and axis of the pie chart.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())
        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=list(colormaps.get_cmap("Paired")(range(len(labels)))),
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title("Endpoint Usage Distribution", fontsize=14)
        plt.tight_layout()
        return fig, ax

    def bargraph(self, color=None):
        """
        Generates a bar graph for endpoint usage.

        Args:
            color (optional): The color of the bars.

        Returns:
            tuple: A tuple containing the figure and axis of the bar graph.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        fig, ax = plt.subplots()
        ax.bar(
            labels,
            height=sizes,
            color=(
                color if color else colormaps.get_cmap("Paired")(range(len(labels)))
            ),
        )
        plt.xlabel("Endpoints", fontsize=12)
        plt.ylabel("Usage Count", fontsize=12)
        plt.title("Endpoint Usage Bar Graph", fontsize=14)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        return fig, ax


class ResponseCodeData:
    """
    Handles data and visualization for response code distribution.

    Attributes:
        data (dict): A dictionary containing response code data.
        url_name (Optional[str]): The URL name associated with the data.
    """

    def __init__(self, data: dict, url_name: Optional[str] = None):
        self.url_name = url_name
        self.data = data

    def piechart(self):
        """
        Generates a pie chart for response code distribution.

        Returns:
            tuple: A tuple containing the figure and axis of the pie chart.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=list(colormaps.get_cmap("Paired")(range(len(labels)))),
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(
            f"{  self.url_name or "Endpoint" } Response Code Distribution", fontsize=14
        )
        plt.tight_layout()
        return fig, ax


class ErrorResponsesData:
    """
    Handles data and visualization for error responses.

    Attributes:
        data (dict): A dictionary containing error response data.
    """

    def __init__(self, data: dict):
        self.data = data

    def bargraph(self, color=None):
        """
        Generates a bar graph for error responses.

        Args:
            color (optional): The color of the bars.

        Returns:
            tuple: A tuple containing the figure and axis of the bar graph.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        fig, ax = plt.subplots()
        ax.bar(
            labels,
            height=sizes,
            color=(
                color if color else colormaps.get_cmap("Paired")(range(len(labels)))
            ),
        )
        plt.xlabel("Endpoints", fontsize=12)
        plt.ylabel("Non 2xx Count", fontsize=12)
        plt.title("Endpoint Error Bar Graph", fontsize=14)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        return fig, ax


class HttpMethodData:
    """
    Handles data and visualization for HTTP method distribution.

    Attributes:
        data (dict): A dictionary containing HTTP method data.
        url_name (Optional[str]): The URL name associated with the data.
    """

    def __init__(self, data: dict, url_name: Optional[str] = None):
        self.data = data
        self.url_name = url_name

    def piechart(self):
        """
        Generates a pie chart for HTTP method distribution.

        Returns:
            tuple: A tuple containing the figure and axis of the pie chart.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        fig, ax = plt.subplots()
        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=list(colormaps.get_cmap("Paired")(range(len(labels)))),
        )
        ax.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f"{ self.url_name or "" }  Http Method Distribution", fontsize=14)
        plt.tight_layout()
        return fig, ax


class RequestOverTimeData:
    """
    Handles data and visualization for requests over time.

    Attributes:
        data (dict): A dictionary containing request data over time.
        interval (str): The time interval for the data (e.g., 'daily', 'weekly', 'monthly').
    """

    def __init__(self, data: dict, interval: str):
        self.data = data
        self.interval = interval

    def linegraph(self):
        """
        Generates a line graph for requests over time.

        Returns:
            tuple: A tuple containing the figure and axis of the line graph.
        """
        labels = list(self.data.keys())
        sizes = list(self.data.values())

        fig, ax = plt.subplots()
        ax.plot(labels, sizes, marker="o")

        plt.xlabel(f"Time ({self.interval})", fontsize=12)
        plt.ylabel("Request Count", fontsize=12)
        plt.title(f"Requests Over Time ({self.interval.capitalize()})", fontsize=14)
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        return fig, ax
