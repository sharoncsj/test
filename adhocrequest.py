#!/usr/bin/env python
from tenable.sc import TenableSC
import pandas as pd
import os
import glob
import numpy as np
from datetime import datetime

#Tenable access
#sc = TenableSC('https://xxxxxx.com')
#sc.login(access_key='ACCESSKEY', secret_key='SECRETKEY')


#read all request in current directory

i = 1
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))


for file in csv_files:

	df = pd.read_excel(file, index_col=None, na_values=['N/A'], usecols="B,E,F", skiprows=2)
	print('Location', file)
	print('File:', file.split("\\")[-1])

	print('data:')
	np_array = df.to_numpy()
	x = np_array.transpose()
	#print(x)
	y = x[0:1]
	jobname= x[2:3,0:1]
	date = x[1:2,0:1]
	#datime = datetime.strptime
	print("Scan Job", i,":",jobname)
	print("Date:", date)
	print("target:", y)
	i = i+1

	







