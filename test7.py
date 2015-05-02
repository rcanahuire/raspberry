


import serial

port = serial.Serial( '/dev/ttyAMA0', 115200 )

port.write( 's' )

data = port.read( 5 )

print 'received 5 bytes: ' , data

port.close()
