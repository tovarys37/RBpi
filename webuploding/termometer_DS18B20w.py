#!/usr/bin/python
#import datetime
import time
from time import gmtime, strftime
import http.client, urllib.request, urllib.parse, urllib.error
from lxml import html
import requests, lxml
import time

#sleep = 5 # how many seconds to sleep between posts to the channel
#key = 'VDXNURGJNEUA4YFZ'  # Thingspeak channel to update
key = 'R59DTI18NXDI9QFR'  # Thingspeak channel to update


def loadTempMasarna():
    page = requests.get('http://teplomer.mk.cvut.cz/')
    tree = html.fromstring(page.content)
    data = tree.xpath('//div[@class="teplota1 "]/text()')
    temp = data[0]
    temp = temp.replace("\n\t\t", "")
    temp = temp.replace("\xa0°C\n\t", "")
    tempT = temp.replace(",", ".")
    #print(float(tempT))
    return float(tempT)

def loadTempStrahov():
    page = requests.get('https://www.in-pocasi.cz/meteostanice/stanice.php?stanice=praha')
    tree = html.fromstring(page.content)
    data = tree.xpath('//table//b/text()')
    temp = data[7]
    temp = temp.replace(" °C", "")
    #print('float>',float(temp))
    return float(temp)
   
def loadTempFS():
    page = requests.get('http://tzb.fsv.cvut.cz/projects/climadata/wx.html')
    tree = html.fromstring(page.content)
    data = tree.xpath('//div[@class="teplota1 "]/text()')
    data = tree.xpath('//div[@class="leftSideBar"]//ul//li/text()')
    temp = data[0]
    temp = temp.replace("Nyní: ", "")
    temp = temp.replace("°C \t\t\r\n", "")
    #print(float(temp))
    return float(temp)


#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer(doma, tempMasarna, tempFS, tempStrahov):
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        #doma, tempMasarna, tempMasarna, TempFS
        casT = time.time();
        params = urllib.parse.urlencode({'field1': casT, 'field2': doma, 'field3':tempMasarna, 'field4':tempFS, 'field5': tempStrahov, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            #conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
            #print("connection OK")
        except:
            print("connection failed")
        break
    

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

  id2 = '28-051693e3fdff'
  name2 = 'DayData20180427_' + id2 +'.txt'
  print(time.time())
  #print ("Temp : " + '{:.3f}'.format(gettemp(id)/float(1000)))
  #f2 = open('' + name2, 'a+')
  ii = 0
  
  #cas = 60*60*24*6
  while (ii<50000):
    #f2 = open('' + name2, 'a+')
    #f2.write('' + str(time.time()) +' {:.3f} \n'.format(gettemp(id2)/float(1000)))
    #f2.close()
      
    tempFS = loadTempFS()
    tempStrahov = loadTempStrahov()    
    tempMasarna = loadTempMasarna()
    thermometer(gettemp(id2)/float(1000), tempMasarna, tempFS, tempStrahov)
    
    print('doma>',(gettemp(id2)/float(1000)), 'tempMasarna>',tempMasarna,'TempFS>',tempFS, 'TempStrahov>',tempStrahov)
    print('online ulozeni zanamu')
    time.sleep(60*2)
    ii = ii + 1
         
  print ("Good bye!")
  
  
  
  