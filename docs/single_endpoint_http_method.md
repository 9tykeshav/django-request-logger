# Single Endpoint HTTP Method

Analyzes HTTP method distribution for a single endpoint and supports piechart representation.

## Function Signature

```python
def single_endpoint_http_method(self, url_name: str) -> HttpMethodData:
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.single_endpoint_http_method(url_name="hello")
fig, ax = data.piechart()
plt.show()
```
