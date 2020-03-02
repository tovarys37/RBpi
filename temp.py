# Write your code here :-)
#!/usr/bin/python

# raspberry termometer DS18B20 python append(time()) csv

from time import time, sleep, strftime
import numpy
import matplotlib.pyplot as plt

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return int(mytemp[1])

  except:
    return 99999

if __name__ == '__main__':

 plt.ion()
 #Matrix = [0];
 T = list();
 cas = list();
 # Script has been called directly
 id = '28-051693e3fdff'
 id = '28-05169416b9ff'
 
 fig = plt.figure()
 plt.clf

 try:
     while True:
         T0= gettemp(id)/float(1000)
         print ("Temp : " + '{:.3f}'.format(T0))
         T.append(T0)
         cas.append(time())
         #sleep(.1)
         plt.plot(cas, T,'.')
         plt.draw
         plt.pause(5.7)
 except KeyboardInterrupt:
     pass

#fig.show()


