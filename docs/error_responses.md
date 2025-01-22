# Error Responses

Analyzes error responses and supports bargraph representation.

## Function Signature

```python
def error_responses(self, exclude: Optional[List[str]] = []) -> ErrorResponsesData:
    """
    Parameters:
    exclude (Optional[List[str]]): A list of endpoint url_names to exclude from the analysis.
    """
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.error_responses(exclude=["health"])
fig, ax = data.bargraph()
plt.show()
```
