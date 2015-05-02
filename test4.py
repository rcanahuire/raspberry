

x = [ 1, False, 1.0, 'h', '????' ]

print 'x: ' , x

print 'typeof x: ' , type( x )

for elem in x:
    print 'elemento: ' , elem
    print 'typeof elem: ' , type( elem )

x = range( 10 )

print 'x: ' , x

for i in range( 100 ):
    print 'i: ' , i

q = 0
while( q < 10 ):
    print 'q: ' , q
    q += 2

while( True ):
    dato = input( 'ingrese 10 para salir: ' )
    if dato == 10:
        break

print 'end'

