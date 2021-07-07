# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:58:22 2021

@author: Administrator
"""

import pandas as pd
from keras.preprocessing.sequence import TimeseriesGenerator
from datetime import datetime
import numpy as np
from sklearn.preprocessing import MinMaxScaler



df = pd.read_csv('./data/daily_treasury_yield_curve_rates.csv', na_values= ['N/A '],skiprows=1, names=['Date','Onemo','Twomo','Threemo','Sixmo',
                                    'Oneyr','Twoyr','Threeyr','Fiveyr','Sevenyr',
                                    'Tenyr','Twentyyr','Thirtyyr'])

del df['Twomo']

df['Date'] = df['Date'].astype('datetime64[ns]')

r = pd.date_range(start=df.Date.min(), end=df.Date.max())

df.set_index('Date').reindex(r).fillna(0.0).rename_axis('Date').reset_index()

datelist = pd.date_range('2000-01-01', periods=7854).tolist()

df_1 = pd.DataFrame(datelist,columns=['Date'])

df_2 = pd.merge(df,df_1,on='Date',how='right')

df_2 = df_2.ffill(axis = 0)

df_2['DayWeek'] = df_2['Date'].dt.day_name()

df_2 = df_2.loc[(df_2['Date'] >= '2010-01-01')]

del df_2['DayWeek']

del df_2['Date']