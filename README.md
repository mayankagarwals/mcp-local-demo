# mcp-local-demo





Test if apis are working as expected: 
```
curl -X 'GET' \
  'http://127.0.0.1:8000/status-distribution?start_time=2022-01-01T00:00:00&end_time=2022-01-02T00:00:00' \
  -H 'accept: application/json'

curl -X 'GET' \
  'http://127.0.0.1:8000/alerts?start_time=2022-01-01T00:00:00&end_time=2022-01-02T00:00:00' \
  -H 'accept: application/json'

```