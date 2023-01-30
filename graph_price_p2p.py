import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os,time
def graph():
    df = pd.read_csv('dict_price.csv')
    df.columns = ['Time', 'binance_Tinkoff_buy', 'binance_Tinkoff_sell', 'binance_sber_buy', 'binance_SBER_sell', 'garantex','moex']
    # df = df.iloc[:,:6]
    # df.columns = ['Time', 'binance_Tinkoff_buy', 'binance_Tinkoff_sell', 'binance_sber_buy', 'binance_SBER_sell', 'garantex']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index)

    plt.figure(figsize=(20, 10))
    plt.plot(df['binance_Tinkoff_buy'],label='binance_Tinkoff_buy', color='blue')
    plt.plot(df['binance_Tinkoff_sell'],label='binance_Tinkoff_sell', color='red')
    plt.plot(df['binance_sber_buy'],label='binance_sber_buy', color='green')
    plt.plot(df['binance_SBER_sell'],label='binance_SBER_sell', color='brown')
    plt.plot(df['garantex'],label='garantex', color='black')
    plt.plot(df['moex'],label='moex', color='orange')
    plt.title("USDT/RUB")
    plt.legend(['binance_Tinkoff_buy', 'binance_Tinkoff_sell','binance_sber_buy','binance_SBER_sell','garantex','moex'])
    plt.savefig('saved_figure.png')
    time.sleep(60)
    os.remove("saved_figure.png")
    
graph()