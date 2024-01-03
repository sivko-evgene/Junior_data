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
        if len(result) < n_size:
            size_adjustment = pd.Series(range(21, 35, 1)).sample(1, replace=True).reset_index(drop=True)
            result = pd.concat([result, size_adjustment])
        return result
