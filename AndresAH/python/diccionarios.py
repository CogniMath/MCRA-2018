# UN DICCIONARIO TIENE LA ESTRUCTURA {clave:valor} 
inventario = {"manzanas": 430, "bananas": 312, "naranjas": 525, "peras": 217}

print()
print('Nuestro inventario es:')
print(inventario)

# CAMBIAR EL VALOR
print()
inventario["naranjas"] = 0

print(inventario)
print('Ahora tenemos', inventario["naranjas"],'naranjas')

#Para un nuevo valor de Bananas podríamos hacer lo siguiente:
inventario["bananas"] += 200

print()
print('Ahora tenemos', inventario["bananas"],'bananas')
print(inventario)

# El método key nos devuelve una lista de todos los claves del diccionario
print()
print('Un arreglo con todas la claves')
print(inventario.keys())

#El método values nos devuelve una lista de todos los valores del diccionario
print()
print('Un arreglo con todos los valores')
print(inventario.values())

# El método items nos devuelve una lista de tuplas
print()
print('Una arreglo de tuplas (klave,valor)')
print(inventario.items())

#Las tuplas a menudo son útiles para obtener tanto la clave como el valor  al mismo tiempo mientras utilizamos un bucle:
print()
print('Ciclo for: ')
for (k,v) in inventario.items():
    if v > 10: print('----> Hay',v,k,'en el stock!!!')
    elif v == 0: print('----> De plano no hay',k,'en el stock!!!')

# el operador in y not in puede comprobar si una clave está en un diccionario:
print()
print('Hay manzanas en el inventario:', "manzanas" in inventario)
print()
print('Hay duraznos en el inventario:',"duraznos" in inventario)
