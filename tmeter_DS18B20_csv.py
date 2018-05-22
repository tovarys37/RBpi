#!/usr/bin/python
import datetime
import time
from time import gmtime, strftime
#import sys

  
import csv
with open('testcsv.csv', 'w') as csvfile:
    fieldnames2 = ['cas', 'temp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames2)
    
    writer.writeheader()
    for i in range(1,5):
        writer.writerow({'cas': str(time.time()), 'temp': i})
        time.sleep(1)


import csv
with open('testcsv.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        

#f = open('testcsv.csv', 'rb')
#reader = csv.reader(f)
#for row in reader
#    print(row)
#    
#f.close()

