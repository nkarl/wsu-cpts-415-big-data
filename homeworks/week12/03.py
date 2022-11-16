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
    df = reader.get_chunk(24)
    print(df.loc[:, 'DATE':'HLY-DEWP-NORMAL'])
