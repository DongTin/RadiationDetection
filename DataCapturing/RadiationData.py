import datetime
import json
import os
import re
from time import sleep

import pypinyin
import requests
from bs4 import BeautifulSoup
from config.crawler import settings


def getCapitalDataFromWeb() -> list:
    response = requests.get(settings.CapitalURL, verify=False)
    html_content = response.content
    capital_datas = []
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    for li_element in li_elements:
        div_capitalName = li_element.find('div', class_='divname').text.strip().split(' (')[0]
        div_detail = li_element.find('div', class_='divname').text.strip().split('(')[-1].split(')')[0]
        div_urlID = li_element.find('div', class_='divname').a['href'].split('_')[1].split('.')[0][:-1]

        capital_info = {
            "Name": div_capitalName,
            "urlID": div_urlID,
            "Detail": div_detail
        }

        capital_datas.append(capital_info)

    return capital_datas


def getNuclearPlantDataFromWeb() -> list:
    response = requests.get(settings.NuclearPlantURL)
    html_content = response.content
    nuclear_plant_data = []
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    for li_element in li_elements:
        div_nuclearPlantName = li_element.find('div', class_='divname').text.strip().split(' (')[0].replace('/', '-')
        div_detail = li_element.find('div', class_='divname').text.strip().split('(')[-1].split(')')[0]
        div_urlID = li_element.find('div', class_='divname').a['href'].split('_')[1].split('.')[0][:-1]

        nuclear_plant_info = {
            "Name": div_nuclearPlantName,
            "urlID": div_urlID,
            "Detail": div_detail
        }

        nuclear_plant_data.append(nuclear_plant_info)

    return nuclear_plant_data


def getCapitalSecondarySiteFromWeb(province_id: int, url_code: str) -> list:
    url = settings.CapitalURL
    new_url = url.replace('listtype0M', f'listsation0_{url_code}M')
    response = requests.get(new_url, verify=False)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    capital_secondary_site_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()

        secondary_info = {
            "Name": div_name,
            "province_id": province_id
        }
        print(secondary_info)
        capital_secondary_site_data.append(secondary_info)

    return capital_secondary_site_data


def getNuclearPlantSecondarySiteFromWeb(plant_id: int, url_code: str) -> list:
    url = settings.NuclearPlantURL
    new_url = url.replace('listtype1M', f'listsation1_{url_code}M')
    response = requests.get(new_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    plant_secondary_site_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()

        secondary_info = {
            "Name": div_name,
            "nuclear_plant_id": plant_id
        }
        print(secondary_info)
        plant_secondary_site_data.append(secondary_info)

    return plant_secondary_site_data


def getCapitalSecondarySiteDayDataFromWeb(Capital) -> list:
    url = settings.CapitalURL
    url_code = Capital.url_code
    new_url = url.replace('listtype0M', f'listsation0_{url_code}M')
    date = datetime.datetime.now()
    response = requests.get(new_url, verify=False)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    capital_secondary_site_day_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        day_data = {
            "capital_secondary_site_name": div_name,
            "date": date,
            "data": numeric_value.group()
        }

        capital_secondary_site_day_data.append(day_data)

    return capital_secondary_site_day_data


def getNuclearPlantSecondarySiteDayDataFromWeb(nuclear_plant) -> list:
    url = settings.NuclearPlantURL
    url_code = nuclear_plant.url_code
    new_url = url.replace('listtype1M', f'listsation1_{url_code}M')
    date = datetime.datetime.now()
    response = requests.get(new_url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    li_elements = soup.find_all('li', class_='datali')
    nuclear_plant_secondary_site_day_data = []
    for li_element in li_elements:
        div_name = li_element.find('div', class_='divname').text.strip()
        div_val = li_element.find('div', class_='divval').span.text.strip()
        numeric_value = re.search(r'\d+', div_val)

        second_level_info = {
            "nuclear_plant_secondary_site_name": div_name,
            "date": date,
            "data": numeric_value.group()
        }

        nuclear_plant_secondary_site_day_data.append(second_level_info)

    return nuclear_plant_secondary_site_day_data
