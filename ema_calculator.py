import btalib
import pandas as pd


def calculate_my_ema(coin_data, smoothing_interval, marker):
    alpha = 2 / (smoothing_interval + 1)
    i = smoothing_interval

    coin_data['my_ema'][smoothing_interval - 1] = sum(coin_data['close_price'][0:smoothing_interval]) / smoothing_interval
    while i < marker + smoothing_interval:
        coin_data['my_ema'][i] = alpha * coin_data['close_price'][i] + (1 - alpha) * coin_data['my_ema'][i - 1]
        i += 1
    coin_data["my_ema"] = pd.to_numeric(coin_data["my_ema"], downcast="float")

    return coin_data

def calculate_btalib_ema(coin_data, smoothing_interval):
    coin_data['ema_btalib'] = btalib.ema(coin_data['close_price'], period=smoothing_interval, _seed=2.3).ema
    coin_data["ema_btalib"] = pd.to_numeric(coin_data["ema_btalib"], downcast="float")

    return coin_data