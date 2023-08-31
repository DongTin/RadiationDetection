from datetime import datetime

from pydantic import BaseModel, validator


class CapitalBase(BaseModel):
    id: int
    name: str
    url_code: str
    detail: str

    class Config:
        orm_mode = True


class CapitalSecondarySiteBase(BaseModel):
    id: int
    name: str
    province_id: int

    class Config:
        orm_mode = True


class NuclearPlantBase(BaseModel):
    id: int
    name: str
    url_code: str
    detail: str

    class Config:
        orm_mode = True


class NuclearPlantSecondarySiteBase(BaseModel):
    id: int
    name: str
    nuclear_plant_id: int

    class Config:
        orm_mode = True


class CapitalSecondarySiteDayDataBase(BaseModel):
    id: int
    capital_secondary_site_id: int
    date: datetime
    data: str

    class Config:
        orm_mode = True


class NuclearPlantSecondarySiteDayDataBase(BaseModel):
    id: int
    nuclear_plant_secondary_site_id: int
    date: datetime
    data: str

    class Config:
        orm_mode = True

