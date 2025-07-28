from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dashboard.router import get_dfo_by_date_range

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


# @router.get("/main")
# def get_base_page(request: Request, info=Depends(get_info_dfo)):   
#     return templates.TemplateResponse("base.html", {"request": request, "info": info})

@router.get("/dfo/{batch_date_start}/{batch_date_end}", response_class=HTMLResponse)
def get_base_page(request: Request, info=Depends(get_dfo_by_date_range)):   
    return templates.TemplateResponse("base.html", {"request": request, "info": info})


