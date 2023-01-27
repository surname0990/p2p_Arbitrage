api_key = '  :      '
url_binance = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

bank_bestch_sber = 'https://www.bestchange.ru/sberbank-to-tether-trc20.html'
bank_bestch_tink = "https://www.bestchange.ru/tinkoff-to-tether-trc20.html"

bank_bestch_trc_sber = "https://www.bestchange.ru/tether-trc20-to-sberbank.html"
bank_bestch_trc_tink = "https://www.bestchange.ru/tether-trc20-to-tinkoff.html"


params_sber = {
    "proMerchantAds": False,
    "page": 1, "rows": 10,
    "payTypes": ["RosBankNew"],
    "countries": [],
    "publisherType": None,
    "fiat": "RUB",
    "tradeType": "BUY",
    "asset": "USDT",
    "merchantCheck": False,
    "transAmount": "100000",
}
params_tink = {
    "proMerchantAds": False,
    "page": 1, "rows": 10,
    "payTypes": ["TinkoffNew"],
    "countries": [],
    "publisherType": None,
    "fiat": "RUB",
    "tradeType": "BUY",
    "asset": "USDT",
    "merchantCheck": False,
    "transAmount": "100000",
}

params_sber_sell = {
    "proMerchantAds": False,
    "page": 1, "rows": 10,
    "payTypes": ["RosBankNew"],
    "countries": [],
    "publisherType": None,
    "fiat": "RUB",
    "tradeType": "SELL",
    "asset": "USDT",
    "merchantCheck": False,
    "transAmount": "100000",
}
params_tink_sell = {
    "proMerchantAds": False,
    "page": 1, "rows": 10,
    "payTypes": ["TinkoffNew"],
    "countries": [],
    "publisherType": None,
    "fiat": "RUB",
    "tradeType": "SELL",
    "asset": "USDT",
    "merchantCheck": False,
    "transAmount": "100000",
}

headers = {
    'accept': '*/*',
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}