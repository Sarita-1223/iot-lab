import time
import random
import urllib

import sqlite3
import time


def sensor_data():
  temp = random.randint(5,45)
  wind = random.randint(55,110)
  moisture = random.randint(5,35)
  rain= random.randint(125,255)
  return temp,wind,moisture,rain
while(1):
  temp,wind,moisture,rain= sensor_data()
  print("Temperature",temp, chr(176) + "C")
  print("windspeed",wind,"%kmh")
  print("Moisture",moisture,"%gmm3")
  print("Rainlevel",rain,"%cm2")
  time.sleep(1.0)
  baseURL = " https://api.thingspeak.com/update?api_key=VKTWOWI8MZ0X1WMI&field1=0"
  g = urllib.urlopen(baseURL + "&field1=%d, &field2=%d, &field3=%d, &field4=%d"%(temp,wind,moisture,rain))
  time.sleep(0.10)
  con = sqlite3.connect("new_db" )
  cursor = con.cursor()
  cursor.execute("DROP TABLE IF EXISTS SENSOR_DATA")
  cursor.execute("CREATE TABLE SENSOR_DATA (SENSOR_TYPE  CHAR(20) , VALUE1 CHAR(20))");
  con.execute("INSERT INTO SENSOR_DATA(SENSOR_TYPE,VALUE1) VALUES (?,?)",("temperature",temp));
  con.commit()
  con.close()
  time.sleep(5)


  





























  



  



