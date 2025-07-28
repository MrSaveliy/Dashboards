import datetime
from pydantic import BaseModel


class INFO_DFO(BaseModel):
    id = int
    batch_name = str
    batch_date = str
    batch_time = str
    batch_sla = str

    class Config:
        from_attributes = True