# Requests Over Time

Analyzes the number of requests over time, supporting daily, weekly, or monthly intervals.

## Function Signature

```python
def requests_over_time(self, interval: str = "daily", exclude: Optional[List[str]] = []) -> RequestOverTimeData:
    """
    Parameters:
    interval (str): The time interval ('daily', 'weekly', or 'monthly').
    exclude (Optional[List[str]]): A list of endpoint url_names to exclude.
    """
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.requests_over_time(interval="weekly", exclude=["admin"])
fig, ax = data.linegraph()
plt.show()
```
