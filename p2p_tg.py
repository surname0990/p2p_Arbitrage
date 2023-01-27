from data import *
from telebot.async_telebot import AsyncTeleBot
import asyncio
import requests
import json, time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver 

bot = AsyncTeleBot(api_key)

@bot.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, """💸 Привет! 💸
 С помощью этого бота ты сможешь узнавать курсы USDT на следующих биржах:
- Binance P2P 
- BestChange
- Garantex
  Для запуска жми: /get_rates""")

@bot.message_handler(commands=['get_rates'])
async def send_rates(message):
    spred = str((float(get_binance(params_sber))- float(get_moex_rates())) / float(get_moex_rates()) *100)
    raznost = str(float(get_binance(params_sber))- float(get_moex_rates()))
    date_ = datetime.now().strftime("%d-%m-%Y %H:%M:%d")
    await bot.send_message(message.chat.id,
    f"""{date_}:            buy         sell 

    🟡 Binance        Tinkoff   {get_binance(params_tink)}      {get_binance(params_tink_sell)}
    🟢 Binance        SBER      {get_binance(params_sber)}      {get_binance(params_sber_sell)}

    🟡 BestChange Tinkoff   {price_bestch(bank_bestch_tink)}      {price_bestch_sell(bank_bestch_trc_tink)}
    🟢 BestChange SBER      {price_bestch(bank_bestch_sber)}      {price_bestch_sell(bank_bestch_trc_sber)}
         
    🔵 Garantex                      {get_garantex_rates()}
    💠 MOEX                           {get_moex_rates()}
                      
Наценка за usdt: {raznost[:4]} rub ({spred[:4]}%)
        """)
def get_binance(params):
    response = requests.post(url=url_binance, headers=headers, json=params, timeout=10).json()
    return response['data'][0]['adv']['price']

def get_garantex_rates():
    url = 'https://garantex.io/api/v2/depth?market=usdtrub'
    response = requests.get(url=url, timeout=60).json()
    return response['asks'][0]['price']
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
        output = output[:5]
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


if __name__ == '__main__':
    asyncio.run(bot.polling())


