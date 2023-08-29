import datetime
import json
import os
import re
from time import sleep

import pypinyin
import requests
from bs4 import BeautifulSoup

URL = "https://data.rmtc.org.cn/gis/listtype0M.html"
URL1 = "https://data.rmtc.org.cn/gis/listtype1M.html"


def getCityIDFromWeb():
    response = requests.get(URL)
    html_content = response.content
    city_data = []
    num = 0
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    for li_element in li_elements:
        div_cityName = li_element.find('div', class_='divname').text.strip().split(' (')[0]
        div_detail = li_element.find('div', class_='divname').text.strip().split('(')[-1].split(')')[0]
        div_urlID = li_element.find('div', class_='divname').a['href'].split('_')[1].split('.')[0][:-1]
        num += 1

        city_info = {
            "Name": div_cityName,
            "cityID": num,
            "urlID": div_urlID,
            "Detail": div_detail
        }

        city_data.append(city_info)

        print("Name:", div_cityName)
        print("cityID:", num)
        print("urlID:", div_urlID)
        print("-" * 40)

        # div_cityName和div_cityID是一一对应的，存入json中
        with open('../Datas/SystemDatas/city_data.json', 'w') as json_file:
            json.dump(city_data, json_file, ensure_ascii=False, indent=4)


def getElectricityIDFromWeb():
    response = requests.get(URL1)
    html_content = response.content
    city_data = []
    num = 0
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    for li_element in li_elements:
        div_electricityName = li_element.find('div', class_='divname').text.strip().split(' (')[0].replace('/', '-')
        div_detail = li_element.find('div', class_='divname').text.strip().split('(')[-1].split(')')[0]
        div_urlID = li_element.find('div', class_='divname').a['href'].split('_')[1].split('.')[0][:-1]
        num += 1

        city_info = {
            "Name": div_electricityName,
            "electricityID": num,
            "urlID": div_urlID,
            "Detail": div_detail
        }

        city_data.append(city_info)

        print("Name:", div_electricityName)
        print("electricityID:", num)
        print("urlID:", div_urlID)
        print("-" * 40)

        # div_cityName和div_cityID是一一对应的，存入json中
        with open('../Datas/SystemDatas/electricity_data.json', 'w') as json_file:
            json.dump(city_data, json_file, ensure_ascii=False, indent=4)


def getCapitalDataFromWeb():
    # 本地获取年月日
    time = datetime.datetime.now()
    dirName = time.strftime("%Y%m%d")

    if not os.path.exists('../Datas/ShowDatas/' + dirName):
        os.mkdir('../Datas/ShowDatas/' + dirName)
    if not os.path.exists('../Datas/ShowDatas/' + dirName + '/citySecondLevel'):
        os.mkdir('../Datas/ShowDatas/' + dirName + '/citySecondLevel')
    if not os.path.exists('../Datas/ShowDatas/' + dirName + '/electricitySecondLevel'):
        os.mkdir('../Datas/ShowDatas/' + dirName + '/electricitySecondLevel')

    response = requests.get(URL)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    capital_data = []

    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip().split(' (')[0]
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        capital_info = {
            "Name": div_name,
            "Value": numeric_value.group()
        }

        capital_data.append(capital_info)

        print("Name:", div_name)
        print("Value:", numeric_value.group())
        print("-" * 40)

        with open('../Datas/ShowDatas/' + dirName + '/capital_data.json', 'w') as json_file:
            json.dump(capital_data, json_file, ensure_ascii=False, indent=4)


def getElectricityDataFromWeb():
    # 本地获取年月日
    time = datetime.datetime.now()
    dirName = time.strftime("%Y%m%d")

    if not os.path.exists('../Datas/ShowDatas/' + dirName):
        os.mkdir('../Datas/ShowDatas/' + dirName)
    if not os.path.exists('../Datas/ShowDatas/' + dirName + '/citySecondLevel'):
        os.mkdir('../Datas/ShowDatas/' + dirName + '/citySecondLevel')
    if not os.path.exists('../Datas/ShowDatas/' + dirName + '/electricitySecondLevel'):
        os.mkdir('../Datas/ShowDatas/' + dirName + '/electricitySecondLevel')

    response = requests.get(URL1)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    electricity_data = []

    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip().split(' (')[0]
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        electricity_info = {
            "Name": div_name,
            "Value": numeric_value.group()
        }

        electricity_data.append(electricity_info)

        print("Name:", div_name)
        print("Value:", numeric_value.group())
        print("-" * 40)

        with open('../Datas/ShowDatas/' + dirName + '/electricity_data.json', 'w') as json_file:
            json.dump(electricity_data, json_file, ensure_ascii=False, indent=4)


def getCitySecondLevelDataFromWeb(CityID: int):
    # 从city_data.json中获取城市ID
    urlID = ''
    fileName = ''
    with open('../Datas/SystemDatas/city_data.json', 'r') as json_file:
        city_data = json.load(json_file)
        for city in city_data:
            if city['cityID'] == CityID:
                urlID = '_' + city['urlID']
                fileName = str(CityID) + pypinyin.slug(city['Name'], style=pypinyin.NORMAL, separator='_') + '.json'
                break

    URL_1 = "https://data.rmtc.org.cn/gis/listsation0" + urlID + "M.html"

    print(URL_1)
    print(fileName)
    response = requests.get(URL_1, verify=False)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    second_level_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        second_level_info = {
            "Name": div_name,
            "Value": numeric_value.group()
        }

        second_level_data.append(second_level_info)

        # print("Name:", div_name)
        # print("Value:", numeric_value.group())
        # print("-" * 40)

        dirName = datetime.datetime.now().strftime("%Y%m%d")
        with open('../Datas/ShowDatas/' + dirName + '/citySecondLevel/' + fileName, 'w') as json_file:
            json.dump(second_level_data, json_file, ensure_ascii=False, indent=4)


def getElectricitySecondLevelDataFromWeb(ElectricityID: int):
    # 从city_data.json中获取城市ID
    urlID = ''
    fileName = ''
    with open('../Datas/SystemDatas/electricity_data.json', 'r') as json_file:
        electricity_data = json.load(json_file)
        for electricity in electricity_data:
            if electricity['electricityID'] == ElectricityID:
                urlID = '_' + electricity['urlID']
                fileName = str(ElectricityID) + pypinyin.slug(electricity['Name'], style=pypinyin.NORMAL,
                                                              separator='_') + '.json'
                break

    URL1_1 = "https://data.rmtc.org.cn/gis/listsation1" + urlID + "M.html"

    print(URL1_1)
    print(fileName)
    response = requests.get(URL1_1, verify=False)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    second_level_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        second_level_info = {
            "Name": div_name,
            "Value": numeric_value.group()
        }

        second_level_data.append(second_level_info)

        # print("Name:", div_name)
        # print("Value:", numeric_value.group())
        # print("-" * 40)

        dirName = datetime.datetime.now().strftime("%Y%m%d")
        with open('../Datas/ShowDatas/' + dirName + '/electricitySecondLevel/' + fileName, 'w') as json_file:
            json.dump(second_level_data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    # # init
    # getCityIDFromWeb()
    # getElectricityIDFromWeb()

    # 获取省会/核电厂数据
    getCapitalDataFromWeb()
    getElectricityDataFromWeb()

    # 获取二级数据
    with open('../Datas/SystemDatas/city_data.json', 'r') as json_file:
        city_data = json.load(json_file)
        for city in city_data:
            getCitySecondLevelDataFromWeb(city['cityID'])
            print('___' * 20)

    with open('../Datas/SystemDatas/electricity_data.json', 'r') as json_file:
        electricity_data = json.load(json_file)
        for electricity in electricity_data:
            getElectricitySecondLevelDataFromWeb(electricity['electricityID'])
            print('___' * 20)
