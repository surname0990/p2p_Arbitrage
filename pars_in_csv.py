from data import *
from telebot.async_telebot import AsyncTeleBot
import requests
import json, time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver 
import csv


def return_info():
    while True:
        date_ = datetime.now().strftime("%d-%m-%Y %H:%M:%d")
        sber_buy = get_binance(params_sber)
        moex = get_moex_rates()
        raznost = float(sber_buy)- float(moex)
        spred = float(raznost) / float(moex) *100
        binance_Tinkoff_buy = get_binance(params_tink)
        binance_Tinkoff_sell =  get_binance(params_tink_sell)
        binance_SBER_sell = get_binance(params_sber_sell)
        garantex = get_garantex_rates()


    #     dict = {
    #    "date": date_ ,                       
    #    "binance_Tinkoff_buy": binance_Tinkoff_buy,
    #    "binance_Tinkoff_sell": binance_Tinkoff_sell,
    # # "bestChange_Tinkoff_buy": price_bestch(bank_bestch_tink),
    # # "bestChange_Tinkoff_sell": price_bestch(bank_bestch_trc_tink),
    #     "binance_SBER_buy": sber_buy,
    #     "binance_SBER_sell": binance_SBER_sell ,
    # # bestChange_SBER_buy: price_bestch(bank_bestch_sber)   
    # # bestChange_SBER_sell: price_bestch(bank_bestch_trc_sber)
    #     "garantex_buy": garantex,
    #     "MOEX": moex,
    #     "raznost": raznost,
    #     "spred": spred,
    #     }    
    #     print(dict)
        
        with open('dict_price.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow((
                date_,
                binance_Tinkoff_buy,
                binance_Tinkoff_sell,
                sber_buy,
                binance_SBER_sell,
                garantex
            ))
        time.sleep(300)
 
        

def get_binance(params):
    response = requests.post(url=url_binance, headers=headers, json=params, timeout=10).json()
    return float(response['data'][0]['adv']['price'])

def get_garantex_rates():
    url = 'https://garantex.io/api/v2/depth?market=usdtrub'
    response = requests.get(url=url, timeout=60).json()
    return float(response['asks'][0]['price'])
    # return 0

def get_moex_rates():
    url = ("https://iss.moex.com/iss/engines/currency/markets/selt/securities.jsonp?"
        "iss.only=securities,marketdata&"
        "securities=CETS:USD000UTSTOM&"
        "lang=ru&iss.meta=off&iss.json=extended&callback=angular.callbacks._gk")

    data = requests.get(url, timeout=60)
    text = data.text[22:len(data.text)-2:]
    json_string = json.loads(text)

    for ss in json_string[1]['securities']:
        output = str(ss['PREVWAPRICE'] )   
        output = float(output[:5])
        return output


def price_bestch(bank):
    rs = requests.get(bank)
    root = BeautifulSoup(rs.content, 'html.parser')
    try:
        tr = root.select('#content_table > tbody > tr')[0]
    except LookupError:  
        print("Исключение IndexError")
        selenium()
        price_bestch(bank)
    else:
        [give_el, get_el] = tr.select('td.bi')
        give = give_el.select_one('.fs').get_text(strip=True)
        output = give[0:5]
    return output

def price_bestch_sell(bank):
    rs = requests.get(bank)
    root = BeautifulSoup(rs.content, 'html.parser')
    try:
        tr = root.select('#content_table > tbody > tr')[0]
    except LookupError:  
        print("Исключение IndexError")
        selenium()
        price_bestch_sell(bank)
    else:
        [give_el, get_el] = tr.select('td.bi')
        get = get_el.get_text(strip=True)
        output = float(get[0:5])
    return output

def selenium():
    EXE_PATH = r'path\to\chromedriver.exe' 
    driver = webdriver.Chrome(executable_path=EXE_PATH) 
    driver.get('https://www.bestchange.ru')
    time.sleep(20)
    driver.quit() 

return_info()