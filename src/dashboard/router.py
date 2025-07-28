from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from dashboard import service
from database.postgres.postgres import get_async_session
router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/get_info_dfo") 
async def get_info_dfo(session: AsyncSession = Depends(get_async_session)):
    try:
        info = await service.get_info_dfo(session=session)
        return info
    except HTTPException as ex:
        print(ex)

@router.get("/get_info_dfo/", response_model=List[dict]) 
async def get_dfo_by_date_range(batch_date_start: str, batch_date_end: str, session: AsyncSession = Depends(get_async_session)):
    try:
        info = await service.get_dfo_by_date_range(batch_date_start=batch_date_start, batch_date_end=batch_date_end, session=session)
        if not info:
            raise HTTPException(
                status_code=404,
                detail="Записи DFO за указанный период не найдены"
            )
        return info
    except HTTPException as ex:
        # Пробрасываем HTTPException дальше (важно!)
        raise ex
    except Exception as e:
        # Ловим любые другие ошибки
        raise HTTPException(
            status_code=500,
            detail=f"Неожиданная ошибка на сервере: {str(e)}"
        )     

# --hand for oracle
# @router.get("/get_info_dfo") 
# def get_info_dfo_o(session: Session = Depends(get_db)):
#     try:
#         info = service.get_info_dfo_o(session=session)
#         return info
#     except HTTPException as ex:
#         print(ex)


# oracle
# @router.get("/get_info_centr_o")
# def get_users(db: Session = Depends(get_db)):
#     return db.query(User).all()