import serial  # pyserial is required


x= 0
uart = serial.Serial("/dev/ttyO1", baudrate=9600, timeout=30)

while x < 100 :
    sent = uart.readline()
    print(sent.decode('utf-8'))
    x += 1
    
exit()