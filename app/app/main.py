from fastapi import FastAPI
from app.routes import auth, views

app = FastAPI()

# Register routes
app.include_router(views.router, tags=["views"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
