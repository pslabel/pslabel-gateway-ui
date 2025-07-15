# app/main.py
from fastapi import FastAPI

app = FastAPI(
    title="PSLabel Gateway",
    description="Web interface for managing PSLabel ESL devices",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to PSLabel Gateway!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "pslabel-gateway"}

# Add this to run with python directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",  # app module:app instance
        host="0.0.0.0",
        port=80,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
