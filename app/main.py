from fastapi import FastAPI

app = FastAPI(
    title="TWCC Cloud Engineering Lab",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message" : "Hello from TWCC Cloud Engineering Lab",
        "status" : "running"
    }

@app.get("/health")
def health() : 
    return {
        "status" : "healthy"
    }