import logging

import pandas as pd

logging.basicConfig(
    filename='test_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(funcName)s || %(message)s', force=True)


class DataPreparation:
    def __init__(self):
        pass

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

    def data_preparation_for_country_generating(self, country: dict) -> pd.DataFrame:
        country = pd.Series(country)
        df = pd.DataFrame(country, columns=['user_quantity'])
        df = df.reset_index()
        df = df.rename(columns={'index': 'country', 'user_quantity': 'user_quantity'})
        df['sum_user_quantity'] = df['user_quantity'].sum()
        return df
