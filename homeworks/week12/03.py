import pandas as pd
# from hdfs import InsecureClient
import os
import csv

datafile = 'normal_hly_sample_temperature.csv'

with open(datafile, 'r') as csvf:
    datareader = csv.reader(csvf)
    for row in datareader:
        print(row)


