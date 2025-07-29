from tempfile import template
from fastapi import FastAPI, Request
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
import uvicorn 
from dashboard.router import router as router_dashboard
from pages.router import router as router_pages

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
app.include_router(router_dashboard)

# === ОБРАБОТЧИК ОШИБОК ===
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "error_404.html",
            {"request": request},
            status_code=404
        )
    return await http_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 422:
        return await templates.TemplateResponse(
            "error_422.html",
            { "request": request},
            status_code=422
        )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 500:
        return await templates.TemplateResponse(
            "error_500.html",
            {"request": request},
            status_code=500
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

