import datetime
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from fastapi import HTTPException

from sqlalchemy import select

from dashboard import models

async def get_info_dfo(session: AsyncSession):
    query = select(models.info_dfo)  
    results = await session.execute(query)
    info = results.mappings().fetchall()  
    return info

async def get_dfo_by_date_range(session: AsyncSession, batch_date_start: str, batch_date_end: str):
    try:
        query = select(models.info_dfo).where(
            models.info_dfo.c.batch_date >= batch_date_start,
            models.info_dfo.c.batch_date <= batch_date_end).order_by(models.info_dfo.c.batch_date)   
        results = await session.execute(query)
        info = results.mappings().fetchall()  
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при запросе к базе данных: {str(e)}")
# heand oracl
# def get_info_dfo_oracle(session: Session):
#     query = select(models.dashboard_DFO)
#     result = session.execute(query)
#     info = result.mappings().fetchall()
#     return info
