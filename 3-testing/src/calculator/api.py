import datetime
from datetime import timezone

import psutil
from calculator import Calculator
from fastapi import FastAPI, HTTPException

app = FastAPI()
calc = Calculator()


@app.get("/add/{x}/{y}")
async def add(x: float, y: float):
    try:
        result = calc.add(x, y)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/divide/{x}/{y}")
async def divide(x: float, y: float):
    try:
        result = calc.divide(x, y)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
async def health():
    try:
        test_add = calc.add(2, 3) == 5
        test_divide = calc.divide(6, 2) == 3

        return {
            "status": "healthy" if (test_add and test_divide) else "degraded",
            "timestamp": datetime.datetime.now(timezone.utc).isoformat(),
            "uptime": psutil.Process().create_time(),
            "memory": {
                "used": psutil.Process().memory_info().rss / 1024 / 1024,
                "percent": psutil.Process().memory_percent(),
            },
        }
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}, 500
