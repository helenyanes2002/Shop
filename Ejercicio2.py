#Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
#permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
#inverso al ingresado+(1)

frutas = []
frutasInversas = []

def validar_si_es_letra(letra):
    if letra.isdigit():
        return False
    else:
        return letra

def agregar_frutas():
    i = 0
    while i < 10:
        nombrefruta = input("Ingresar la fruta: ")
        fruta = validar_si_es_letra(nombrefruta)
        if fruta:
            frutas.append(fruta)
            i = i+1
        else:
            print("Ingrese una fruta valida")
    print(frutas)
    return frutas


def invertir_frutas(x):
    for fruntaInversa in reversed(x):
        frutasInversas.append(fruntaInversa)
    return frutasInversas


print(invertir_frutas(agregar_frutas()))

