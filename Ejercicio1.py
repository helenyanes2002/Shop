#-Construir un programa que permita ingresar N (cantidad digitada por el
#usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
#ingresados (+1)

multiplos_de_dos = []
multiplos_de_tres = []


numero = input("Digite la cantidad: ")


def validar_si_es_numero(numero):
    if numero.isdigit():
        return numero
    return False

def castear_numero(numero):
    return int(numero)

while not validar_si_es_numero(numero):
    print("Ingrese un numero valido: ")
    numero = input("Digite la cantidad:  ")
    validar_si_es_numero(numero)

numero_casteado = castear_numero(numero)

for numero in range(numero_casteado):
    numeroIngresado = input("Ingrese el número: ")

    while not validar_si_es_numero(numeroIngresado):
        print("Ingrese un número valido: ")
        numeroIngresado = input("Ingrese el número: ")
        validar_si_es_numero(numeroIngresado)

    numeroIngresadoCasteado = castear_numero(numeroIngresado)

    if numeroIngresadoCasteado % 2 == 0:
        multiplos_de_dos.append(numeroIngresadoCasteado)

    if numeroIngresadoCasteado % 3 == 0:
        multiplos_de_tres.append(numeroIngresadoCasteado)


print(f"La cantidad de multiplos de dos digitados es: {len(multiplos_de_dos)}")
print(f"La cantidad de multiplos de tres digitados es: {len(multiplos_de_tres)}")
