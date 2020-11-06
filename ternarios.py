#Si something vale True, imprimir una x, si vale False, imprimir una y
something = True

#Forma con la cual trabajamos, pero podemos simplificar este código, para
#ello podemos usar Ternarios
#V1
if something == True:
    print('x')
else:
    print('y')

#V2
if something:
    print('x')
else:
    print('y')

#V3 - con operadores ternarios, son como if, pero mucho más reducidos
print('x' if something == True else 'y')

#V4 - con operadores ternarios, como estamos comparando que something es True
#y something esta inicializado con el valor True, quitamos el comparar
#Mejor solución
print('x' if something else 'y')

#If que no tienen if
#V5, trabajamos con una tupla, 0 es False y 1 es True, tales valores los
#definimos como índices, como something esta inicializado con el valor 1
#verificamos el elemento que se encuentra con el índice 1, es x
print(('y', 'x')[something])

#V6, en este caso trabajamos con una lista, sigue el mismo patrón
print(['y', 'x'][something])

#V7, trabajamos con un diccionario, la lógica es la misma
print({True: 'x', False: 'y'}[something])


#Tengo una función que me va a devolver algo
def return_something(a):
    if a == 1:
        return 'Pepe'
    return 'Panchito'

print(return_something(1))
print(5 + True)

