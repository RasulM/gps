import serial
import time

s1 = serial.Serial('/dev/ttyO1',9600, timeout = 0.1)
s2 = serial.Serial('/dev/ttyO2',9600, timeout = 0.1)
s3 = serial.Serial('/dev/ttyO3',9600, timeout = 0.1)
s4 = serial.Serial('/dev/ttyO4',9600, timeout = 0.1)
s5 = serial.Serial('/dev/ttyO5',9600, timeout = 0.1)

while 1:
	s1.write('This is UART1!\n')
	s2.write('This is UART2!\n')
	s3.write('This is UART3!\n')
	s4.write('This is UART4!\n')
	s5.write('This is UART5!\n')

	print 'UART1: ', s1.readline()
	print 'UART2: ', s2.readline()
	print 'UART3: ', s3.readline()
	print 'UART4: ', s4.readline()
	print 'UART5: ', s5.readline()

	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	time.sleep(0.5)