import datetime

from sqlalchemy import Column, String, DateTime, Text, Integer
from sqlalchemy.sql import func
from db.database import db
from db.database import Base


class BaseModel(Base):
    __abstract__ = True

    create_date = Column(DateTime, default=func.now(), doc='创建时间')
    remarks = Column(String(1000), nullable=True, default=None, doc='备注信息')
    abnormal_flag = Column(String(1), default='0', doc='异常标记')

    class Meta:
        database = db


class Capital(BaseModel):
    __tablename__ = "capital_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True, default=None, doc='省份名称')
    url_code = Column(String(64), nullable=True, default=None, doc='省份url编码')
    detail = Column(Text, nullable=True, doc='省份辐射判断依据站点')


class CapitalSecondarySite(BaseModel):
    __tablename__ = "capital_secondary_site_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True, default=None, doc='省份二级站点名称')
    province_id = Column(Integer, nullable=True, default=None, doc='所属省份id')


class NuclearPlant(BaseModel):
    __tablename__ = "nuclear_plant_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True, default=None, doc='核电站名称')
    url_code = Column(String(64), nullable=True, default=None, doc='核电站url编码')
    detail = Column(Text, nullable=True, doc='核电站辐射判断依据站点')


class NuclearPlantSecondarySite(BaseModel):
    __tablename__ = "nuclear_plant_secondary_site_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=True, default=None, doc='核电站二级站点名称')
    nuclear_plant_id = Column(Integer, nullable=True, default=None, doc='所属核电站id')


class CapitalSecondarySiteDayData(BaseModel):
    __tablename__ = "capital_secondary_site_day_data_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    capital_secondary_site_id = Column(Integer, nullable=True, default=None, doc='所属二级站点id')
    date = Column(DateTime, default=func.now(), doc='日期')
    data = Column(Text, nullable=True, doc='数据')


class NuclearPlantSecondarySiteDayData(BaseModel):
    __tablename__ = "nuclear_plant_secondary_site_day_data_table"

    # id为主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    nuclear_plant_secondary_site_id = Column(Integer, nullable=True, default=None, doc='所属核电站二级站点id')
    date = Column(DateTime, default=func.now(), doc='日期')
    data = Column(Text, nullable=True, doc='数据')