#-Construir un programa para ir de compras en un supermercado que
#permita la construcción del siguiente MENU:
#1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
#2. Digitar 2 para mostrar todos los productos registrados (+0.4)
#3. Digitar 3 para permitir buscar por código un producto y editar el precio
#de este (+0.4)
#4. Digitar 4 para permitir buscar por código un producto y eliminar el
#producto (+0.4)
#5. Digitar 0 para SALIR

productos = []


def validar_si_es_un_numero(numero):
    if numero.isdigit():
        return numero

    else:
        return False


def preguntar_preferencia():
    opcion_preferencia = input("presione s para si o n para no: ")
    return opcion_preferencia.lower()


def castear_string_a_entero(numero_castear):
    return int(numero_castear)


def mostrar_opciones():
    print("Digitar 1 para recibir {código, nombre, precio} de un producto")
    print("Digitar 2 para mostrar todos los productos registrados")
    print("Digitar 3 para permitir buscar por código un producto y editar el precio")
    print("Digitar 4 para permitir buscar por código un producto y eliminar el")
    print("Digitar 0 para SALIR")
    opcion_seleccionada = input("digite opcion: ")
    return opcion_seleccionada


def mostrar_opciones_casteadas():
    opcion_seleccionada = mostrar_opciones()
    validar_opcion = validar_si_es_un_numero(opcion_seleccionada)
    while not validar_opcion:
        print("ingrese un numero valido")
        opcion_seleccionada = mostrar_opciones()
        validar_opcion = validar_si_es_un_numero(opcion_seleccionada)

    opcion_casteada = castear_string_a_entero(validar_opcion)

    return opcion_casteada


def agregar_producto(codigo, nombre, precio):
    objeto_agregar = dict(codigo=codigo, nombre=nombre, precio=precio)
    productos.append(objeto_agregar)
    print("producto agregado correctamente")
    return True


def bucar_producto(codigo):
    for i in productos:
        codigo_objeto = i["codigo"]
        if codigo_objeto == codigo:
            return i


def editar_producto(producto, precio):
    producto["precio"] = precio
    return True


def eliminar(producto):
    productos.remove(producto)
    return True


def crud(opcion_escojidaInt):
    global opcion_seleccionada
    opcion_seleccionada = opcion_escojidaInt

    while opcion_seleccionada >= 5:
        print("seleccione una opcion valida")
        opcion_seleccionada = mostrar_opciones_casteadas()

    while opcion_seleccionada != 0:
        global preferencia
        if opcion_seleccionada == 1:
            codigo = input("digite codigo:")
            nombre = input("dijite nombre:")
            precio = input("dijite precio:")
            if (agregar_producto(codigo, nombre, precio)):
                print("desea agregar otro producto?")
                preferencia = preguntar_preferencia()
                while preferencia == 's':
                    codigo = input("digite codigo:")
                    nombre = input("dijite nombre:")
                    precio = input("dijite precio:")
                    agregar_producto(codigo, nombre, precio)
                    print("desea agregar otro producto?")
                    preferencia = preguntar_preferencia()

                while preferencia != 'n' and preferencia != 's':
                    print("seleccione una opcion valida")
                    preferencia = preguntar_preferencia()

                if preferencia == 'n':
                    opcion_seleccionada = mostrar_opciones_casteadas()



        elif opcion_seleccionada == 2:
            print(productos)
            print("desea volver a ver las opciones?")
            preferencia = preguntar_preferencia()
            if preferencia == 's':
                opcion_seleccionada = mostrar_opciones_casteadas()

            elif preferencia == 'n':
                break
            else:
                print("seleccione una opcion valida")
                preferencia = preguntar_preferencia()




        elif opcion_seleccionada == 3:

            if not productos:
                print("no hay productos a mostrar debes añadir productos")
                print("desea añadir?")
                preferencia = preguntar_preferencia()
                while preferencia == 's':
                    codigo = input("digite codigo:")
                    nombre = input("dijite nombre:")
                    precio = input("dijite precio:")
                    agregar_producto(codigo, nombre, precio)
                    print("desea agregar otro producto?")
                    preferencia = ""
                    preferencia = preguntar_preferencia()

                while preferencia != 'n' and preferencia != 's':
                    print("seleccione una opcion valida")

                    preferencia = preguntar_preferencia()

                if preferencia == 'n':
                    opcion_seleccionada = mostrar_opciones_casteadas()

            print(f"lista de productos\n{productos}")
            codigo_producto = input("escriba codigo de producto  a editar:")
            producto = bucar_producto(codigo_producto)
            if producto:
                precio = input("ingrese precio a editar:")
                if (editar_producto(producto, precio)):
                    print("producto editado correctamente")
                    print(productos)
                    print("desea volver al menu principal?")
                    preferencia = preguntar_preferencia()
                    if preferencia == 's':
                        opcion_seleccionada = mostrar_opciones_casteadas()

                    elif preferencia == 'n':
                        break
                    else:
                        print("seleccione una opcion valida")
                        preferencia = preguntar_preferencia()


            else:
                print("producto no encontrado")
                print("desea volver al menu principal?")
                preferencia = preguntar_preferencia()
                if preferencia == 's':
                    opcion_seleccionada = mostrar_opciones_casteadas()

                elif preferencia == 'n':
                    break

                else:
                    print("seleccione una opcion valida")
                    preferencia = preguntar_preferencia()



        elif opcion_seleccionada == 4:
            if not productos:
                print(f"no hay productos a mostrar debes añadir productos")
                print("desea añadir?")
                preferencia = preguntar_preferencia()
                if preferencia == "s":
                    codigo = input("digite codigo: ")
                    nombre = input("dijite nombre: ")
                    precio = input("dijite precio: ")
                    objeto_agregar = dict(codigo=codigo, nombre=nombre, precio=precio)
                    productos.append(objeto_agregar)
                    print("producto añadido correctamente")
                    print(productos)

                elif preferencia == "n":
                    break

                else:
                    print("seleccione una opcion valida")
                    preferencia = preguntar_preferencia()

            print(f"lista de productos \n{productos}")
            codigo_producto = input("escriba codigo de producto  a eliminar: ")
            producto = bucar_producto(codigo_producto)

            if producto:

                if eliminar(producto):
                    print("eliminado correctamente")
                    print(f"productos restantes \n {productos}")
                    print("desea volver al menu principal?")
                    preferencia = preguntar_preferencia()
                    if preferencia == 's':
                        opcion_seleccionada = mostrar_opciones_casteadas()

                    elif preferencia == 'n':
                        break
                    else:
                        print("seleccione una opcion valida")
                        preferencia = preguntar_preferencia()




            else:
                print("producto no encontrado")
                print("desea volver al menu principal?")
                preferencia = preguntar_preferencia()
                if preferencia == 's':
                    opcion_seleccionada = mostrar_opciones_casteadas()

                elif preferencia == 'n':
                    break

                else:
                    print("seleccione una opcion valida")
                    preferencia = preguntar_preferencia()


# main
crud(mostrar_opciones_casteadas())
