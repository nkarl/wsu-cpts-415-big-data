import pandas as pd
# from hdfs import InsecureClient
import os

# client_hdfs = InsecureClient('http://hdfs_ip:50070')

datafile = 'normal_hly_sample_temperature.csv'

# with client_hdfs.read('/user/hdfs/' + datafile, encoding = 'utf-8') as reader:
i = 0
# for chunk in pd.read_csv(reader, sep=',', chunksize=24):
for chunk in pd.read_csv(datafile, sep=',', chunksize=24):
        df    = chunk
        today = df['DATE'][i].split(' ')[0]
        temp  = round(df['HLY-TEMP-NORMAL'].sum() / df.shape[0], 2)
        dew   = round(df['HLY-DEWP-NORMAL'].sum() / df.shape[0], 2)
        print(f"{today}\t{temp}, {dew}")
        i += 24

