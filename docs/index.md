# Request Logs Viewer Documentation

You can use the `RequestLogsViewer()` inside any of your views, or even away from your Django project directory. Using it away from the Django directory requires you to make the `RequestLogsViewer()` aware of the project's settings. You can achieve this by:

```python
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

# Setup Django
django.setup()

from django_request_logger.log_viewer import RequestLogsViewer
import matplotlib.pyplot as plt

# Create an instance of RequestLogsViewer
view_request_logs = RequestLogsViewer()
# refer to further documentation
```

## Basic structure

Each graph plotting method returns a tuple of `(Figure, Axes)`. You can further edit the graph labels or customize the plot. Refer to [Figures](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html) and [Axes](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html) returned by [subplots()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html).

You can either call:

```python
view_request_logs = RequestLogsViewer()
logs = view_request_logs.endpoint_usage()
fig, ax = logs.piechart()
fig, ax = logs.bargraph()

plt.show()
```

Or you can call `fig.imsave()` as needed if you want to save a particular plot. Refer to the Figure docs mentioned above.

make sure for `exclude` parameter in different methods you mention the url_name parameter you gave in your `urls.py` for different endpoints

## Available Functions

1. [Endpoint Usage](endpoint_usage.md)
   - Graphs: Piechart, Bargraph
2. [Response Code Distribution](resp_code_distribution.md)
   - Graphs: Piechart
3. [Error Responses](error_responses.md)
   - Graphs: Bargraph
4. [HTTP Method Distribution](http_method_distribution.md)
   - Graphs: Piechart
5. [Single Endpoint HTTP Method](single_endpoint_http_method.md)
   - Graphs: Piechart
6. [Requests Over Time](requests_over_time.md)
   - Graphs: Linegraph
