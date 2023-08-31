import json
import httpx
from urllib.parse import parse_qs
import urllib3
import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from config.config import settings
import db.curd as curd
from db.database import Base, engine, SessionLocal
from starlette.responses import RedirectResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/admin/init", dependencies=[Depends(get_db)])
async def init_admin(db: Session = Depends(get_db)):
    # 忽视verity=False警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # 初始化一级与二级站点信息
    # curd.getCapitalData(db)
    # curd.getNuclearPlantData(db)
    # curd.getCapitalSecondarySiteData(db)
    # curd.getNuclearPlantSecondarySiteData(db)

    # # 获取监测站日数据
    # tempList = curd.getCapitalList(db)
    # for x in tempList:
    #     curd.getCapitalSecondarySiteDayData(db, x)
    #     print(x.name)
    #     print(x.id)
    #     print('------------------'*5)

    # 获取核电站日数据
    # tempList = curd.getNuclearPlantList(db)
    # for x in tempList:
    #     curd.getNuclearPlantSecondarySiteDayData(db, x)
    #     print(x.name)
    #     print(x.id)
    #     print('------------------' * 5)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)
