import unittest
import pandas as pd
from random import randrange
from ema_calculator import calculate_my_ema, calculate_btalib_ema

# 25 values for tests
close_price_test = [1, 2.3, 3.4, 4, 5, 6.7, 7.8, 8.9, 9.1, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.1, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.1]
df_test = pd.DataFrame(columns=['close_price', 'my_ema', 'ema_btalib'])

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pd.options.mode.chained_assignment = None

    def test_1(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])

    def test_2(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])

    def test_4(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])

    def test_5(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])

    def test_6(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])


    def test_7(self):
        smoothing_interval_test = randrange(23)
        marker_test = 24 - smoothing_interval_test

        df_test['close_price'] = close_price_test
        my_ema = calculate_my_ema(df_test, smoothing_interval_test, marker_test)
        ema_bta_lib = calculate_btalib_ema(df_test, smoothing_interval_test)

        self.assertEqual(my_ema['my_ema'][smoothing_interval_test+marker_test-1], ema_bta_lib['ema_btalib'][smoothing_interval_test+marker_test-1])

if __name__ == '__main__':
    unittest.main()



