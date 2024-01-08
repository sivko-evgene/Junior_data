import logging

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid
import names

logging.basicConfig(
    filename='test_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(funcName)s || %(message)s', force=True)


class DataGeneratorsUser:
    def __init__(self):
        pass

    def id_generator(self, n_size: int) -> pd.Series:
        result = []
        while len(result) != n_size:
            result.append(uuid.uuid1())
        return pd.Series(result)

    def name_generator(self, n_size: int) -> pd.Series:
        result = []
        for _ in range(n_size):
            result.append(names.get_full_name())
        return pd.Series(result)

    def age_generator(self, n_size: int) -> pd.Series:
        n_size_10_20 = int(n_size * 22 / 100)
        n_size_21_35 = int(n_size * 35 / 100)
        n_size_36_50 = int(n_size * 28 / 100)
        n_size_51_65 = int(n_size * 15 / 100)
        age_10_20 = pd.Series(range(10, 20, 1)).sample(n_size_10_20, replace=True).reset_index(drop=True)
        age_21_35 = pd.Series(range(21, 35, 1)).sample(n_size_21_35, replace=True).reset_index(drop=True)
        age_36_50 = pd.Series(range(10, 20, 1)).sample(n_size_36_50, replace=True).reset_index(drop=True)
        age_51_65 = pd.Series(range(10, 20, 1)).sample(n_size_51_65, replace=True).reset_index(drop=True)
        result = pd.concat([age_10_20, age_21_35, age_36_50, age_51_65])
        while len(result) != n_size:
            size_adjustment = pd.Series(range(21, 35, 1)).sample(1, replace=True).reset_index(drop=True)
            result = pd.concat([result, size_adjustment])
        return result

    def country_generator(self, n_size: int) -> pd.Series:
        country = {"China": 283820000, "Japan": 68500000, "USA": 104470000, "South_Korea": 15410000, "UK": 16310000,
                   "Mexico": 31070000, "Indonesia": 50960000, "France": 15620000, "India": 201100000,
                   "Germany": 16790000,
                   "Spain": 12900000, "Italy": 12910000, "Canada": 9910000, "Brazil": 42500000, "Argentina": 10830000,
                   "Philippines": 10620000, "Russia": 30400000, "Thailand": 6740000, "Vietnam": 13770000,
                   "Hong_Kong": 1920000, "Netherlands": 3530000, "Singapore": 1410000, "Malaysia": 4920000,
                   "Turkey": 15160000, "Poland": 6550000, "Australia": 5500000, "Saudi_Arabia": 3630000,
                   "Sweden": 2820000,
                   "Belgium": 2390000, "Norway": 1630000, "Austria": 1630000, "Ireland": 1290000,
                   "Switzerland": 1780000,
                   "Denmark": 1220000, "Finland": 1440000, "Czech_Republic": 2040000, "Israel": 1130000,
                   "South_Africa": 6440000, "Portugal": 1680000, "Romania": 1960000, "Hungary": 1180000,
                   "Slovakia": 770000,
                   "Serbia": 600000, "Croatia": 520000, "Lithuania": 320000, "Bulgaria": 590000, "Slovenia": 270000,
                   "Estonia": 160000, "Latvia": 230000}
        country = pd.Series(country)
        df = pd.DataFrame(country, columns=['user_quantity'])
        df = df.reset_index()
        df = df.rename(columns={'index': 'country', 'user_quantity': 'user_quantity'})
        df['sum_user_quantity'] = df['user_quantity'].sum()
        df['interest'] = df['user_quantity'] * 100 / df['sum_user_quantity']
        df['sample'] = round(df['interest'], 2) * 100
        df['sample'] = df['sample'].astype(int)
        try:
            result = []
            n = 0
            for i in df['country']:
                k = [i] * df['sample'][n]
                n += 1
                result.extend(k)
        except KeyError:
            pass
        result = pd.Series(result).sample(n_size, replace=True).reset_index(drop=True)
        while len(result) != n_size:
            size_adjustment = pd.Series('China').sample(1, replace=True).reset_index(drop=True)
            result = pd.concat([result, size_adjustment])
        return result
