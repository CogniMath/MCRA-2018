# EJEMPLOS DEL USO DE ARREGLOS EN PYTHON

# ---------------- CREANDO UN ARREGLO -------------------

arr = [10,20,40,'Hola mundo',[1,2,3],(0,1)]

print('------')
print(arr)
print()
print('Accediendo a los elementos del arreglo')
print(arr[0])
print(arr[3])
print(arr[5])
print()
print('Podemos tambien rebanar el arreglo')
print(arr[1:4])
print(arr[3:])
print(arr[ :3])
print(arr[-4:])
print(arr[-3:-1])

# ---------------- CICLOS FOR -------------------

FRUTAS = ['Manzanas','Platanos','Mango','Naranja','Papaya']

for i in FRUTAS:
    if i == 'Naranja':
        print('Fruta: ', i)
        print('-----> ME ENCANTA EL JUGO DE NARANJA')
    else:
        print('Fruta: ', i)

# ---------------- OPERACIONES -------------------   

NUMEROS = [10.,3.,6.,8.,3.,7.,9.,2.,5.]

print()
print('AGREGAR ELEMENTOS CON append()')
NUMEROS.append(1)
print(NUMEROS)
print()
print('QUITAR UNA ENTRADA EN PARTICULAR CON pop')
NUMEROS.pop(3)
print(NUMEROS)
print()
print('SABER EL NUM. DE ELEMENTOS CON len')
print('yo tengo',len(NUMEROS), 'numeros')
print()
print('SABER EN QUE ENTRADA ESTA LA FRUTA')
print('El 7 esta en la entrada',NUMEROS.index(7))
print()
print('ODENANDO LAS ENTRADAS')
NUMEROS.sort()
print(NUMEROS)
print()
print('DE REVERSA')
NUMEROS.reverse()
print(NUMEROS)
print()
print('EL MINIMO Y EL MAXIMO')
print('El minimo es:',min(NUMEROS),'y el maximo es', max(NUMEROS))     