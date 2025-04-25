# mcp-local-demo


1. Clone the repo 
```
your preferred way of cloning like git clone 
```
2. Install uv 
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
3. 


Add the following in your user settings (json) of VS code

```
{
    "mcp": {
        "servers": {
            "my-mcp-demo": {
                "command": "uv",
                "args": [
                  "--directory",
                  "/path/mcp-local-demo",
                  "run",
                  "main.py"
                ],
              }
        }
    }
}


  

```

4. 
Run the following query 
```
Can you give me what is the distribution of status codes my service received yesterday?


```