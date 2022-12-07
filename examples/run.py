
from pynmeagps import NMEAReader
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


# msg = NMEAReader.parse('$GNGGA,083301.00,1358.0162538,N,10026.7303514,E,4,25,0.8,4.006,M,-31.715,M,1.0,0499*72\r\n')
# print(msg)
# print(msg.msgID) #get the message ID
# print(msg.lat, msg.lon, msg.time) #get the latitude





