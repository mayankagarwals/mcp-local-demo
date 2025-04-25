from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

app = FastAPI()

class StatusDistribution(BaseModel):
    code_400: int
    code_500: int

class AlertType(str, Enum):
    CPU_THRESHOLD_BREACHED = "CPU threshold breached beyond 90%"
    MEMORY_THRESHOLD_BREACHED = "Memory usage surpassed 80%"
    DISK_SPACE_LOW = "Disk space remaining less than 10%"
    NETWORK_LATENCY_HIGH = "Network latency surpassed 200ms"
    SERVICE_UNAVAILABLE = "Backend service unavailable"
    HIGH_ERROR_RATE = "High error rate detected"

@app.get("/status-distribution", response_model=StatusDistribution)
def get_status_distribution(
    start_time: datetime = Query(..., description="Start timestamp"),
    end_time: datetime = Query(..., description="End timestamp")
):
    # Static data for now
    return StatusDistribution(code_400=100, code_500=240)

@app.get("/alerts", response_model=list[AlertType])
def get_alerts(
    start_time: datetime = Query(..., description="Start timestamp"),
    end_time: datetime = Query(..., description="End timestamp")
):
    # Static list of meaningful alerts for now
    alerts = [
        AlertType.CPU_THRESHOLD_BREACHED,
        AlertType.MEMORY_THRESHOLD_BREACHED,
        AlertType.DISK_SPACE_LOW,
        AlertType.NETWORK_LATENCY_HIGH,
        AlertType.SERVICE_UNAVAILABLE,
        AlertType.HIGH_ERROR_RATE
    ]
    return alerts


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)