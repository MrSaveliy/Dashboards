from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn 
from dashboard.router import router as router_dashboard
from pages.router import router as router_pages

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router_pages)
app.include_router(router_dashboard)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

