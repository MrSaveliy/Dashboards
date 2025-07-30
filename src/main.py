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
    # Для 404 возвращаем свою страницу
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "error_404.html",
            {"request": request},
            status_code=404
        )
    # Для других HTTP-ошибок можно сделать универсальную страницу
    return templates.TemplateResponse(
        "error_http.html",
        {"request": request, "status_code": exc.status_code, "detail": exc.detail},
        status_code=exc.status_code
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Страница для ошибок валидации (422)
    return templates.TemplateResponse(
        "error_422.html",
        {"request": request, "errors": exc.errors()},
        status_code=422
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    # Все непредусмотренные ошибки выдаем страницу 500
    return templates.TemplateResponse(
        "error_500.html",
        {"request": request, "error": str(exc)},
        status_code=500
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

