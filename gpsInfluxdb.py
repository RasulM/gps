import datetime
import time
import serial  # pyserial is required
from micropyGPS import MicropyGPS #https://github.com/inmcm/micropyGPS
from influxdb import InfluxDBClient #python3 -m pip install influxdb

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('gps')
gps = MicropyGPS()
uart = serial.Serial("/dev/ttyO1", baudrate=9600, timeout=30)
sent = uart.readline().decode('utf-8')

while 1:
    sent = uart.readline().decode('utf-8')
    for x in sent:
        gps.update(x)
        
    json_body = [
    {
        "measurement": "gpsEvents",
        "tags": {
            "user": "RESTPI",
            "Id": "6b 65 74 74 65 72 69 6e 67 20 69 73 20 45 70 69 63 20 4f 77 4f"
        },
        "time": str('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())),
        "fields": {
            "fix_type":str(gps.fix_type),
            "latitude": gps.latitude_string(),
            "latitude_Minutes":float(gps.latitude[1]),
            "longitude": gps.longitude_string(),
            "longitude_Minutes":float(gps.longitude[1]),
            "speed":float(gps.speed[2]),
            "direction":str(gps.compass_direction())
            
        }
    }
]

    print(json_body)
# uncomment line below to log
   # client.write_points(json_body)
    



