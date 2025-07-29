from datetime import datetime
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from fastapi import HTTPException

from sqlalchemy import select

from dashboard import models

async def get_info_dfo(session: AsyncSession):
    try:
        current_datetime = datetime.now().strftime('%Y-%m-%d')
        first_day_of_current_month = current_datetime[:-2] + '01'
        query = select(models.info_dfo).where(
                models.info_dfo.c.batch_date >= first_day_of_current_month,
                models.info_dfo.c.batch_date <= current_datetime).order_by(models.info_dfo.c.batch_date)
        results = await session.execute(query)
        rows = results.mappings().fetchall()
        info = [dict(row) for row in rows]
        if not info:
            raise HTTPException(status_code=404, detail="Информация DFO не найдена")
        return info
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Ошибка при запросе к базе данных: {str(ex)}")

async def get_dfo_by_date_range(session: AsyncSession, batch_date_start: str, batch_date_end: str):
    try:
        query = select(models.info_dfo).where(
            models.info_dfo.c.batch_date >= batch_date_start,
            models.info_dfo.c.batch_date <= batch_date_end).order_by(models.info_dfo.c.batch_date)   
        results = await session.execute(query)
        rows = results.mappings().fetchall()
        info = [dict(row) for row in rows]
        if not info:
                raise HTTPException(status_code=404, detail="Информация DFO не найдена")
        return info
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Ошибка при запросе к базе данных: {str(ex)}")
# heand oracl
# def get_info_dfo_oracle(session: Session):
#     query = select(models.dashboard_DFO)
#     result = session.execute(query)
#     info = result.mappings().fetchall()
#     return info
