




def average( notas ):
    total = 0
    for nota in notas:
        total += nota
    total = total / len( notas )
    return total

def average2( notas ):
    total = 0
    for i in range( len( notas ) ):
        total += notas[i]
    total = total / len( notas )
    return total
    

notas = [10,15,14,13,16]

print 'promedio de las notas: ' , average( notas )
print 'promedio de las notas: ' , average2( notas )

# DICTIONARIES

student1 = { 'name' : 'roberto', 'notas' : [15,16,17,18,19,20] }

print 'nombre del estudiante: ' , student1['name']
print 'notas del estudiante: ' , student1['notas']
print 'promedio del estudiante: ' , average2( student1['notas'] )






