import datetime

from sqlalchemy.orm import Session

from DataCapturing.RadiationData import (getCapitalDataFromWeb, getNuclearPlantDataFromWeb,
                                         getCapitalSecondarySiteFromWeb, getNuclearPlantSecondarySiteFromWeb,
                                         getCapitalSecondarySiteDayDataFromWeb,
                                         getNuclearPlantSecondarySiteDayDataFromWeb)
from db.model import Capital, NuclearPlant, CapitalSecondarySite, CapitalSecondarySiteDayData, \
    NuclearPlantSecondarySiteDayData, NuclearPlantSecondarySite


def getCapitalData(db: Session):
    capitals = getCapitalDataFromWeb()
    capitals_temp = []
    for capital in capitals:
        if db.query(Capital).filter(Capital.name == capital['Name']).first() is None:
            capitals_temp.append(capital)
            db_capital = Capital(name=capital['Name'], url_code=capital['urlID'], detail=capital['Detail'],
                                 create_date=datetime.datetime.now(), remarks='爬虫爬取', abnormal_flag='0')
            db.add(db_capital)
            db.commit()
            db.refresh(db_capital)

    return capitals_temp


def getCapitalDataByID(db: Session, capitalID: int):
    capital = db.query(Capital).filter(Capital.id == capitalID).first()
    return capital


def getCapitalList(db: Session):
    capitals = db.query(Capital).all()
    return capitals


def getCapitalSecondarySiteData(db: Session):
    capitals = db.query(Capital).all()
    secondaryDataTemp = []
    for capital in capitals:
        secondaryDatas = getCapitalSecondarySiteFromWeb(capital.id, capital.url_code)
        for secondaryData in secondaryDatas:
            if db.query(CapitalSecondarySite).filter(
                    CapitalSecondarySite.name == secondaryData['Name']).first() is None:
                db_capitalSecondarySite = CapitalSecondarySite(name=secondaryData['Name'],
                                                               province_id=secondaryData['province_id'],
                                                               create_date=datetime.datetime.now(), remarks='爬虫爬取',
                                                               abnormal_flag='0')
                db.add(db_capitalSecondarySite)
                db.commit()
                db.refresh(db_capitalSecondarySite)
                secondaryDataTemp.append(secondaryData)

    return secondaryDataTemp


def getCapitalSecondarySiteDataByID(db: Session, capitalSecondarySiteID: int):
    capitalSecondarySite = db.query(CapitalSecondarySite).filter(
        CapitalSecondarySite.id == capitalSecondarySiteID).first()
    return capitalSecondarySite


def getCapitalSecondarySiteDataByName(db: Session, capitalSecondarySiteName: str):
    capitalSecondarySite = db.query(CapitalSecondarySite).filter(
        CapitalSecondarySite.name == capitalSecondarySiteName).first()
    return capitalSecondarySite


def getCapitalSecondarySiteList(db: Session):
    capitalSecondarySites = db.query(CapitalSecondarySite).all()
    return capitalSecondarySites


def getCapitalSecondarySiteDataByProvinceID(db: Session, provinceID: int):
    capitalSecondarySites = db.query(CapitalSecondarySite).filter(
        CapitalSecondarySite.province_id == provinceID).all()
    return capitalSecondarySites


def getCapitalSecondarySiteDayData(db: Session, capital):
    datas = getCapitalSecondarySiteDayDataFromWeb(capital)
    for data in datas:
        db_data = CapitalSecondarySiteDayData(capital_secondary_site_id=getCapitalSecondarySiteDataByName(db, data['capital_secondary_site_name']).id,
                                              date=data['date'], data=data['data'],
                                              create_date=datetime.datetime.now(), remarks='爬虫爬取', abnormal_flag='0')
        db.add(db_data)
        db.commit()
        db.refresh(db_data)

    return datas


def getNuclearPlantData(db: Session):
    nuclearPlants = getNuclearPlantDataFromWeb()
    nuclearPlants_temp = []
    for nuclearPlant in nuclearPlants:
        if db.query(NuclearPlant).filter(NuclearPlant.name == nuclearPlant['Name']).first() is None:
            nuclearPlants_temp.append(nuclearPlant)
            db_nuclearPlants = NuclearPlant(name=nuclearPlant['Name'], url_code=nuclearPlant['urlID'],
                                       detail=nuclearPlant['Detail'], create_date=datetime.datetime.now(),
                                       remarks='爬虫爬取', abnormal_flag='0')
            db.add(db_nuclearPlants)
            db.commit()
            db.refresh(db_nuclearPlants)

    return nuclearPlants_temp


def getNuclearPlantDataByID(db: Session, nuclearPlantID: int):
    nuclearPlant = db.query(NuclearPlant).filter(NuclearPlant.id == nuclearPlantID).first()
    return nuclearPlant


def getNuclearPlantList(db: Session):
    nuclearPlants = db.query(NuclearPlant).all()
    return nuclearPlants


def getNuclearPlantSecondarySiteData(db: Session):
    nuclearPlants = db.query(NuclearPlant).all()
    secondaryDataTemp = []
    for nuclearPlant in nuclearPlants:
        secondaryDatas = getNuclearPlantSecondarySiteFromWeb(nuclearPlant.id, nuclearPlant.url_code)
        for secondaryData in secondaryDatas:
            if db.query(NuclearPlantSecondarySite).filter(
                    NuclearPlantSecondarySite.name == secondaryData['Name']).first() is None:
                db_capitalSecondarySite = NuclearPlantSecondarySite(name=secondaryData['Name'],
                                                               nuclear_plant_id=secondaryData['nuclear_plant_id'],
                                                               create_date=datetime.datetime.now(), remarks='爬虫爬取',
                                                               abnormal_flag='0')
                db.add(db_capitalSecondarySite)
                db.commit()
                db.refresh(db_capitalSecondarySite)
                secondaryDataTemp.append(secondaryData)

    return secondaryDataTemp


def getNuclearPlantSecondarySiteDataByID(db: Session, nuclearPlantSecondarySiteID: int):
    nuclearPlantSecondarySite = db.query(CapitalSecondarySite).filter(
        CapitalSecondarySite.id == nuclearPlantSecondarySiteID).first()
    return nuclearPlantSecondarySite


def getNuclearPlantSecondarySiteDataByName(db: Session, nuclearPlantSecondarySiteName: str):
    nuclearPlantSecondarySite = db.query(NuclearPlantSecondarySite).filter(
        NuclearPlantSecondarySite.name == nuclearPlantSecondarySiteName).first()
    return nuclearPlantSecondarySite


def getNuclearPlantSecondarySiteList(db: Session):
    nuclearPlantSecondarySites = db.query(CapitalSecondarySite).all()
    return nuclearPlantSecondarySites


def getNuclearPlantSecondarySiteDataByNuclearPlantID(db: Session, nuclearPlantID: int):
    nuclearPlantSecondarySites = db.query(CapitalSecondarySite).filter(
        CapitalSecondarySite.nuclear_plant_id == nuclearPlantID).all()
    return nuclearPlantSecondarySites


def getNuclearPlantSecondarySiteDayData(db: Session, nuclearPlant):
    datas = getNuclearPlantSecondarySiteDayDataFromWeb(nuclearPlant)
    for data in datas:
        db_data = NuclearPlantSecondarySiteDayData(
            nuclear_plant_secondary_site_id=getNuclearPlantSecondarySiteDataByName(db, data['nuclear_plant_secondary_site_name']).id,
            date=data['date'], data=data['data'],
            create_date=datetime.datetime.now(), remarks='爬虫爬取', abnormal_flag='0')
        db.add(db_data)
        db.commit()
        db.refresh(db_data)

    return datas
