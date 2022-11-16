import pandas as pd
# from hdfs import InsecureClient
import os
import csv
import sys

def read_input(file):
    for line in file:
        yield line


datafile = 'normal_hly_sample_temperature.csv'

i = 0
for chunk in pd.read_csv(datafile, sep=',', chunksize=24):
    df    = chunk
    today = df['DATE'][i].split(' ')[0]
    temp  = round(df['HLY-TEMP-NORMAL'].sum() / df.shape[0], 2)
    dew   = round(df['HLY-DEWP-NORMAL'].sum() / df.shape[0], 2)
    print(f"{today}\t{temp}, {dew}")
    i += 24

