#!/usr/bin/python
import datetime
import time
from time import gmtime, strftime

def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    #print('Device >' + id + '< has been found')
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
  # Script has been called directly
  #id = '28-03168bfbafff'
  #print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))
  id = '28-051693e3fdff'
  print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))
  
  print(time.time())
  #print(time.localtime())
  #id1 = '28-03168bfbafff'
  #name1 = 'DayData20180420' + id1 +'.txt'
  id2 = '28-051693e3fdff'
  name2 = 'DayData20180427_' + id2 +'.txt'
     
    
  #f = open('' + name1, 'a+')
  f2 = open('' + name2, 'a+')
  ii = 0
  print('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id2)/float(1000)))
  
  #cas = 60*60*24*6
  while (ii<144):
    i=0
    while (i<60): #ukladame kazdou hodinu
      #print(i)  
      #f.write('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id1)/float(1000)))
      #print('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id1)/float(1000)))
      f2.write('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id2)/float(1000)))
      time.sleep(60)
      i = i + 1
    ii = ii + 1
    #f.close()
    f2.close()
    #f = open('' + name1, 'a+')
    f2 = open('' + name2, 'a+')
    print ("Ulozeni c. "+ str(ii))
    print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
    print('' + str(time.time()) +' {:.2f} \n'.format(gettemp(id2)/float(1000)))
                  
  print ("Good bye!")
  #f.close()
  f2.close()
  
  