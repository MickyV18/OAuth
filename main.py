from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import auth
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


app = FastAPI()

# Register auth router (if needed for other routes)
app.include_router(auth.router, prefix="/auth")

templates = Jinja2Templates(directory="app/templates")

# Directly serve the index.html at the root route
@app.get("/", response_class=HTMLResponse)
def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

