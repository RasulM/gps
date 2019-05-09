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
            "user": "automousPI",
            "brushId": "6969"
        },
        "time": str('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())),
        "fields": {
            "fix_type":str(gps.fix_type),
            "latitude": gps.latitude_string(),
            "longitude": gps.longitude_string(),
            "speed":str(gps.speed_string('kph')),
            "direction":str(gps.compass_direction())
        }
    }
]

    print(json_body)
    client.write_points(json_body)
    time.sleep(1)


