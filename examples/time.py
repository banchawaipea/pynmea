
from pynmeagps import NMEAReader
from datetime import datetime


file = open('./data_nmea.txt', encoding='utf-8')

for line in file.readlines():
    msg = NMEAReader.parse(line)
    if msg.msgID == 'GGA':
        print(msg)
        print(msg.quality) #get the quality of the fix
        if msg.quality == 4:
            print('Fix')
        elif msg.quality == 5:
            print('Float')
        elif msg.quality == 1:
            print('Single')
        print(msg.msgID) #get the message ID
        print(msg.lat, msg.lon, msg.time) #get the latitude

date_String = "7.12.2022 08:40:12 UTC +0700"
dt_format = datetime.strptime(date_String, '%d.%m.%Y %H:%M:%S %Z %z')
print("Date with Timezone Name::", dt_format)


timestamp = dt_format.timestamp()
print("timestamp is::", timestamp)
# msg = NMEAReader.parse('$GNGGA,083301.00,1358.0162538,N,10026.7303514,E,4,25,0.8,4.006,M,-31.715,M,1.0,0499*72\r\n')
# print(msg)
# print(msg.msgID) #get the message ID
# print(msg.lat, msg.lon, msg.time) #get the latitude





