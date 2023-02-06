from data import *
from telebot.async_telebot import AsyncTeleBot
import requests
import json, time
from datetime import datetime
from bs4 import BeautifulSoup
import csv

def return_info(time_ = 300):
    while True:
        date_ = datetime.now().strftime("%m-%d-%Y %H:%M:%d") 
        sber_buy = get_binance(params_sber)
        moex = get_moex_rates()
        binance_Tinkoff_buy = get_binance(params_tink)
        binance_Tinkoff_sell =  get_binance(params_tink_sell)
        binance_SBER_sell = get_binance(params_sber_sell)
        garantex = get_garantex_rates()
        name_date_csv = datetime.now().strftime("%m-%d-%Y") + ".csv"
        list_usdt =(date_,
                binance_Tinkoff_buy,
                binance_Tinkoff_sell,
                sber_buy,
                binance_SBER_sell,
                garantex,
                moex)
        with open(name_date_csv, 'a', encoding='utf-8', newline='') as file:
            print(name_date_csv)
            writer = csv.writer(file)
            writer.writerow(list_usdt)
        with open("main.csv", 'a', encoding='utf-8', newline='') as main_csv:
            print("main.csv")
            writer = csv.writer(main_csv)
            writer.writerow(list_usdt)
        time.sleep(time_)
 
def get_binance(params):
    response = requests.post(url=url_binance, headers=headers, json=params, timeout=10).json()
    return float(response['data'][0]['adv']['price'])

def get_garantex_rates():
    url = 'https://garantex.io/api/v2/depth?market=usdtrub'
    response = requests.get(url=url, timeout=60).json()
    return float(response['asks'][0]['price'])

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

return_info()