# Response Code Distribution

Analyzes response code distribution and supports piechart representation.

## Function Signature

```python
def resp_code_distribution(self, url_name: Optional[str] = None, exclude: Optional[List[str]] = []) -> ResponseCodeData:
    """
    Parameters:
    url_name (Optional[str]): The name of the endpoint to filter the response codes.
    exclude (Optional[List[str]]): A list of endpoint url_names to exclude from the analysis.
    """
```

## Example

```python
from django_request_logger.log_viewer import RequestLogsViewer

viewer = RequestLogsViewer()
data = viewer.resp_code_distribution(url_name="login_endpoint")
fig, ax = data.piechart()
plt.show()
```
