import time
import logging
import argparse
import warnings
import pandas as pd
import plotly.express as px
from ema_calculator import calculate_my_ema, calculate_btalib_ema
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client

df_btcusdt = pd.DataFrame(columns=['unix_time', 'close_price', 'my_ema', 'ema_btalib'])
df_ethusdt = pd.DataFrame(columns=['unix_time', 'close_price', 'my_ema', 'ema_btalib'])
df_bnbbtc =  pd.DataFrame(columns=['unix_time', 'close_price', 'my_ema', 'ema_btalib'])

prev_t_btcusdt = 0
prev_t_ethusdt = 0
prev_t_bnbbtc = 0

prev_c_btcusdt = 0
prev_c_ethusdt = 0
prev_c_bnbbtc = 0

flag = True
pd.options.mode.chained_assignment = None
warnings.simplefilter("ignore")
def checkflag():
    global flag
    if(len(df_btcusdt['close_price']) >= smoothing_interval + marker) and \
            (len(df_ethusdt['close_price']) >= smoothing_interval + marker) and \
            (len(df_bnbbtc['close_price']) >= smoothing_interval + marker):
        flag = False

def save_time_and_price(message):
    global prev_t_btcusdt, prev_t_ethusdt, prev_t_bnbbtc, prev_c_btcusdt, \
        prev_c_ethusdt, prev_c_bnbbtc, df_btcusdt, df_bnbbtc, df_ethusdt
    if message['stream'] == 'btcusdt@kline_1m':
        if (int(message['data']['k']['t']) != prev_t_btcusdt) and (prev_t_btcusdt != 0):
            df_btcusdt = df_btcusdt.append({'close_price': prev_c_btcusdt, 'unix_time': prev_t_btcusdt}, ignore_index = True)
        prev_t_btcusdt = int(message['data']['k']['t'])
        prev_c_btcusdt = float(message['data']['k']['c'])

    if message['stream'] == 'ethusdt@kline_1m':
        if (int(message['data']['k']['t']) != prev_t_ethusdt) and (prev_t_ethusdt != 0):
            df_ethusdt = df_ethusdt.append({'close_price': prev_c_ethusdt, 'unix_time': prev_t_ethusdt}, ignore_index = True)
        prev_t_ethusdt = int(message['data']['k']['t'])
        prev_c_ethusdt = float(message['data']['k']['c'])

    if (message['stream'] == 'bnbbtc@kline_1m'):
        if (int(message['data']['k']['t']) != prev_t_bnbbtc) and (prev_t_bnbbtc != 0):
            df_bnbbtc = df_bnbbtc.append({'close_price': prev_c_bnbbtc, 'unix_time': prev_t_bnbbtc}, ignore_index = True)
        prev_t_bnbbtc = int(message['data']['k']['t'])
        prev_c_bnbbtc = float(message['data']['k']['c'])

    checkflag()

marker = int(input("Enter the number of values you want to get "))  # Number of EMA's values which you want to get.
smoothing_interval = int(input("Enter the smoothing interval for exponential moving average "))  # Number of close prices which will be used to calculate the first EMA's values


# uses for input docker's agruments
# parser = argparse.ArgumentParser(description="Smoothing interval and marker")
# parser.add_argument("-m", dest="marker", default=5, type=int)
# parser.add_argument("-s", dest="smoothing_interval", default=3, type=int)
# args = parser.parse_args()
# marker = args.marker
# smoothing_interval = args.smoothing_interval


ws_client = Client()
ws_client.start()

ws_client.instant_subscribe(
    stream=['btcusdt@kline_1m',
            'ethusdt@kline_1m',
            'bnbbtc@kline_1m'],
    callback=save_time_and_price,
)

while flag:
    time.sleep(1)

ws_client.stop()

logging.basicConfig(level=logging.INFO)

df_btcusdt = calculate_my_ema(df_btcusdt, smoothing_interval, marker)
df_btcusdt = calculate_btalib_ema(df_btcusdt, smoothing_interval)
logging.info('BTCUSDT\n' + df_btcusdt[['my_ema', 'ema_btalib']].to_string() + '\n')
fig = px.line(df_btcusdt[smoothing_interval:], y=['my_ema', 'ema_btalib'], x='unix_time', title='BTCUSDT')
fig.write_image('charts/btcusdt.png')


df_ethusdt = calculate_my_ema(df_ethusdt, smoothing_interval, marker)
df_ethusdt = calculate_btalib_ema(df_ethusdt, smoothing_interval)
logging.info('ETHUSDT\n' + df_ethusdt[['my_ema', 'ema_btalib']].to_string() + '\n')
fig = px.line(df_ethusdt[smoothing_interval:], y=['my_ema', 'ema_btalib'], x='unix_time', title='ETHUSDT')
fig.write_image('charts/ethusdt.png')


df_bnbbtc = calculate_my_ema(df_bnbbtc, smoothing_interval, marker)
df_bnbbtc = calculate_btalib_ema(df_bnbbtc, smoothing_interval)
logging.info('BNBBTC\n' + df_ethusdt[['my_ema', 'ema_btalib']].to_string() + '\n')
fig = px.line(df_bnbbtc[smoothing_interval:], y=['my_ema', 'ema_btalib'], x='unix_time', title='BNBBTC')
fig.write_image('charts/bnbbtc.png')
