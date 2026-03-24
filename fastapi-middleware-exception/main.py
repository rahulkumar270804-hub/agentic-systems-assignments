from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import time

app = FastAPI()

# Middleware: Log request + measure time
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    print(f"Incoming request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"Completed in {process_time:.4f} seconds")

    return response


# Normal route
@app.get("/hello")
def hello():
    return {"message": "Hello World"}


# Custom 404 handler
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Route not found"}
    )