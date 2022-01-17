def cuentaRegresiva(num):
    numeros = []
    for i in range (num, -1, -1):
        numeros.append(i)
    print(numeros)

cuentaRegresiva(20)

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

imprimir_y_devolver([4, 3])

def primero_mas_longitud(lista):
    return lista[0] + len(lista)

print(primero_mas_longitud([1,2,3,4,5]))

def valores_mayores_que_el_segundo(lista):
    nuevaLista = []
    numerosMayores = 0
    if len(lista)<2:
        return False
    else:
        for i in lista:
            if i > lista[1]:
                nuevaLista.append(i)
                numerosMayores= numerosMayores+1
        print("Hay", numerosMayores, "numeros mayores que", lista[1])
        return nuevaLista

print(valores_mayores_que_el_segundo([5]))

def length_and_value(size, value):
    lista = []
    for i in range (size):
        lista.append(value)
    return lista

print(length_and_value(4, 7))