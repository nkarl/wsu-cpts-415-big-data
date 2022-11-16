import pandas as pd
# from hdfs import InsecureClient
import os
import csv
import sys

def read_input(file):
    for line in file:
        yield line


datafile = 'normal_hly_sample_temperature.csv'

with pd.read_csv(datafile, sep=',', iterator=True) as reader:
    df    = reader.get_chunk(24)
    today = df['DATE'][0].split(' ')[0]
    temp  = df['HLY-TEMP-NORMAL'].sum() / df.shape[0]
    dew   = df['HLY-DEWP-NORMAL'].sum() / df.shape[0]
    print(f"{today}\t{temp}, {dew}")

