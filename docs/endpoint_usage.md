# Endpoint Usage

Analyzes endpoint usage.

## Function Signature

```python
def endpoint_usage(self, exclude: Optional[List[str]] = []) -> EndpointUsageData:
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.endpoint_usage(exclude=["admin"])
fig, ax = data.piechart()
plt.show()
```
