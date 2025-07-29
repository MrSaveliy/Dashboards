from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dashboard.router import get_dfo_by_date_range, get_info_dfo

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/dashboards_list")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/dfo", response_class=HTMLResponse)
def get_base_page(request: Request, info=Depends(get_info_dfo)):
    return templates.TemplateResponse("dashboard_dfo.html", {"request": request, "info": info})

@router.get("/dfo/search", response_class=HTMLResponse)
def get_base_page(request: Request, info=Depends(get_dfo_by_date_range)):
        return templates.TemplateResponse("dashboard_search.html", {"request": request, "info": info})

 

