from fastapi import FastAPI
from routes import auth, views
import uvicorn

app = FastAPI()

app.include_router(views.router, tags=["views"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")