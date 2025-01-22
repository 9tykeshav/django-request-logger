# HTTP Method Distribution

Analyzes HTTP method distribution and supports piechart representation.

## Function Signature

```python
def http_method_distribution(self, exclude: Optional[List[str]] = []) -> HttpMethodData:
    """
    Parameters:
    exclude (Optional[List[str]]): A list of endpoint url_names to exclude from the analysis.
    """
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.http_method_distribution(exclude=["health"])
fig, ax = data.piechart()
plt.show()
```
