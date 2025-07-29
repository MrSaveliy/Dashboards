from sqlalchemy import  ForeignKey, Table, MetaData, Column, Integer, String, Date, Text
from database.postgres.postgres import Base

metadata = MetaData()

class INFO_DFO(Base):
    __tablename__ = "info_dfo", 
    metadata,
    id = Column(Integer, primary_key=True)
    batch_name = Column(String, unique=False)
    batch_date = Column(String, unique=False)
    batch_time = Column(String, unique=False)
    batch_sla  = Column(String, unique=False)

info_dfo= Table (
    "info_dfo", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("batch_name", String),
    Column("batch_date", String),
    Column("batch_time", String),
    Column("batch_sla", String)
)

