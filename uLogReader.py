#Things we will need:
#1. File Path
#2. File Name
#3. File Extension
#4. Desired topic

#import pyulog
from pyulog import info, ulog2csv, params, messages, extract_gps_dump
import os #for dissecting os path
import inspect
import sys
import tempfile
from ddt import ddt, data
import unittest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from matplotlib import pyplot as plt
from matplotlib import cbook as cbook
import numpy as np
import pandas as pd
import csv
import math
import time
import datetime
import argparse


#Step 1: Identify the file directory
filePath=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print(filePath)
#Step 2: Identify the file name
fileName="18_37_37.ulg"
#Step 3: Convert ulog to csv for ease of reading
if os.path.isdir(filePath):
	print("FilePath exists")
if not os.path.isdir(filePath+"/CSV"):
	print("Making CSV folder")
	os.mkdir(filePath+"/CSV")
csvPath=filePath+"/CSV/"
if os.path.isdir(csvPath):
	print("CSV folder exists")
#Step 4: Convert ulog to csv
csvName=csvPath+fileName[:-4]+"_actuator_controls_0_0.csv"
if not os.path.isfile(csvName):
	print("Converting ulog to csv")
	ulog2csv.convert_ulog2csv(filePath+"/"+fileName, None, filePath+"/CSV", ",", False)

#Step 5: Read the csv file labeled "actuator_controls_0"

print("CSV NAME :: " + csvName)
if os.path.isfile(csvName):
	print("CSV file exists")
fname=cbook.get_sample_data(csvName,asfileobj=False)
with cbook.get_sample_data(csvName) as file:
	msft = pd.read_csv(file)

msft.plot("timestamp",["control[0]","control[1]","control[2]","control[3]","control[4]","control[5]","control[6]","control[7]"],subplots=True)
msft.plot("timestamp",["control[0]","control[1]","control[2]","control[3]","control[4]","control[5]","control[6]","control[7]"],subplots=False)
plt.show()

