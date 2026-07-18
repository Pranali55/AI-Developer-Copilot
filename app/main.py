from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from app.routers.review import router as review_router
from app.routers.security import router as security_router
from app.routers.tests import router as tests_router
from app.routers.upload import router as upload_router
from app.routers.explain import router as explain_router
from app.routers.documentation import router as documentation_router
from app.routers.convert import router as convert_router
# Create FastAPI app
app = FastAPI(
    title="AI Developer Copilot",
    version="1.0.0"
)

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# Register Routers
app.include_router(upload_router)
app.include_router(explain_router)
app.include_router(review_router)
app.include_router(security_router)
app.include_router(documentation_router)
app.include_router(tests_router)
app.include_router(convert_router)

# Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )