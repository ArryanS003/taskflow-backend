from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello! My backend is working."
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }