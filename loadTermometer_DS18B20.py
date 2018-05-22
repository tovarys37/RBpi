#!/usr/bin/python
import datetime
from datetime import date
import time
from time import gmtime, strftime
import string

import numpy as np
import matplotlib as mpl
mpl.use('tkagg')    #YAAA!!  this finally makes the Damn thing work
import matplotlib.pyplot as plt

aktualniCas = time.time()
print('Now: ',time.strftime('%X %x %Z'))

#print(time.localtime())
#id1 = '28-03168bfbafff'
#name1 = 'DayData20180420' + id1 +'.txt'
#id2 = '28-051693e3fdff'
#name2 = 'DayData20180420' + id2 +'.txt'

filename = 'DayData20180427_28-051693e3fdff.txt'

#import glob, os
#os.chdir("chuj")
#for file in glob.glob("*.txt"):
#    print(file)
    
#with open(file_eval_id) as f:
#eval_ids = [int(line) for line in f]

#f2 = open(filename, "r")
#data = f2.read()
#print(data(2))
#numb = string.atoi(data.split())
#numbers = f2.readline()
#numb = string.atoi(numbers.split())


count = 0
#for line in open(filename).xreadlines(  ): count += 1
for line in open(filename): count += 1
print('number of measurements: ',count)
#count +=1

cas = [0]*count
temp = [0]*count



with open(filename) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       #print(line.split())
       sup = line.split()
       cas[cnt-1] = float(sup[0])
       temp[cnt-1] = float(sup[1])
       #print(type (float(sup[1]))) 
       line = fp.readline()
       cnt += 1
       

#print(cas)
#print(temp)
#fig, (ax1, ax2) = plt.subplots(1, 2)
#my_plotter(ax1, data1, data2, {'marker':'x'})
#my_plotter(ax2, data3, data4, {'marker':'o'})

#plt.plot(cas, temp)#,'.')
       
casA = np.asarray(cas)
tempA = np.asarray(temp) 
timeNow = casA[1]
print('start: ',time.ctime(timeNow))
print('end: ',time.ctime(casA[-1]))

#print(tempA[1:11])
tempA[(np.where(tempA>90))]=20
tempA[(np.where(tempA<10))]=20
#whereMAX = np.where(tempA>90);
#print(whereMAX[:])
#tempA[whereMAX[:]-1]=20

casA=casA-timeNow
casA = casA/60/60

#print(np.where(casA == casA.max()))

plt.plot(casA, tempA)
#plt.scatter(casA, temp)
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
#plt.xlim((-1000, dataset[-1][0]+1000))


plt.show()

#plt.plot(cas, temp)

#x = np.arange(0, 5, 0.1);
#y = np.sin(x)
#plt.plot(x, y)


#infile = open(filename, 'r')
#numbers = [float(line) for line in infile.readlines()]
#infile.close()
#mean = sum(numbers)/len(numbers)
#print (mean)



#f2.close()
print ("end")


     
  