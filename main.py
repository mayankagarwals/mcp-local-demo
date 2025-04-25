from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")


@mcp.tool()
async def get_status_distribution(start_time: str, end_time: str) -> dict:
    """Get distribution of status codes for a given time period.

    Args:
    start_time: Start timestamp in ISO format (e.g. '2022-01-01T00:00:00')
    end_time: End timestamp in ISO format (e.g. '2022-01-02T00:00:00')

    Returns:
    dict: Distribution of status codes with counts.
    """
    # Static data for now
    return {
        "code_400": 100,
        "code_500": 240
    }

@mcp.tool()
async def get_alerts(start_time: str, end_time: str) -> str:
    """Get a list of alerts activated between two timestamps.

    Args:
    start_time: Start timestamp in ISO format (e.g. '2022-01-01T00:00:00')
    end_time: End timestamp in ISO format (e.g. '2022-01-02T00:00:00')

    Returns:
    str: List of meaningful alerts.
    """
    # Static list of meaningful alerts for now
    alerts = [
        "CPU threshold breached beyond 90%",
        "Memory usage surpassed 80%",
        "Disk space remaining less than 10%",
        "Network latency surpassed 200ms",
        "Backend service unavailable",
        "High error rate detected"
    ]
    return "\n---\n".join(alerts)


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')