import numpy as np

a = np.arange(12)

print()
print('Se genera un arreglo con 12 numeros:')
print(a)

a = np.arange(3,12,2)

print()
print('Arreglo del 3 al 12 cada 2 numeros')
print(a)

a = np.linspace(11.,12.,11)

print()
print('Tambien podemos usar linspace')
print(a)

print()
print('Y podemos hacer operaciones en los arreglos')

theta = np.linspace(0,np.pi,3)
b     = np.sin(theta)
print(b)
