import pandas as pd
# from hdfs import InsecureClient
import os

# client_hdfs = InsecureClient('http://hdfs_ip:50070')

datafile = 'normal_hly_sample_temperature.csv'

# with client_hdfs.read('/user/hdfs/' + datafile, encoding = 'utf-8') as reader:
i=0; DAY=24
for chunk in pd.read_csv(datafile, sep=',', chunksize=DAY):
        today = chunk['DATE'][i].split(' ')[0]
        temp  = round(chunk['HLY-TEMP-NORMAL'].sum() / chunk.shape[0], 2)
        dew   = round(chunk['HLY-DEWP-NORMAL'].sum() / chunk.shape[0], 2)
        print(f"{today}\t{temp}, {dew}")
        i += DAY

