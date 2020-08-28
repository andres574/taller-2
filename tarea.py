# /////////////////////////////////EJERCISIO 1 //////////////////////////////////

# numeros = [1, 6, 8, 3, 5, 4, 7, 2]

# def recorrer():
#     print("lista de numeros")
#     for i in numeros:
#         print(i)

# recorrer()
# numeros.sort()
# print(f"lista ordenada: {numeros}")

# print(f"la longitud de la lista es {len(numeros)}")

# def buscarelemento(num):
#     numero = False
#     for i in numeros:
#         if num == i:
#             numero = True
#     if numero == True:
#         print("numero encontrado")
#     else:
#         print("numero no encontrado")


# buscarelemento(int(input("Valor a buscar: ")))


# /////////////////////////////////EJERCISIO 2 //////////////////////////////////


# lista = []
# while len(lista) < 120:
#     numero = int(input("ingrese un numero: "))
#     lista.append(numero)
# print("lista llena ")
# print(lista)


# /////////////////////////////////EJERCISIO 3 //////////////////////////////////

# texto = ""
# while texto == "":
#     texto = input("ingresa una frase: ")

# print(texto.upper())


# /////////////////////////////////EJERCISIO 4 //////////////////////////////////


# def variables():
#     lista = ['uno', 'dos', 'tres']
#     string = "ejersicio 4"
#     entero = 6
#     boleano = True
#     print(f"el tipo de dato de {lista} es {type(lista)}")
#     print(f"el tipo de dato de {string} es {type(string)}")
#     print(f"el tipo de dato de {entero} es {type(entero)}")
#     print(f"el tipo de dato de {boleano} es {type(boleano)}")
# variables()


# ///////////////////////////////////////EJERCISIO 5//////////////////////////////////////////////////

# def conte():
#     contenido = [
#         {'nombre': 'ACCION',
#          'JUEGOS': ['GTA', 'COD', 'PUG']
#          },
#         {'nombre': 'AVENTURA',
#          'JUEGOS': ['ASSINS', 'CRASH', 'pricipe of persia']
#          },
#         {'nombre': 'DEPORTES',
#          'JUEGOS': ['FIFA 21', 'PRO 21', 'MOTO GP 21']
#          },
#     ]

#     for i in contenido:
#         print("Categoria: " + str(i["nombre"] + "\n"))

#         for j in i["JUEGOS"]:
#             print('--------------------------')
#             print(j)

#         print("")


# conte()


# ///////////////////////////////////////EJERCISIO 6//////////////////////////////////////////////////
# contactos = [
#     {'nombre': 'antonio',
#      'cedula': 1010101,
#      'carrera': 'inginieria'
#      }
# ]

# editar = input("que elemento quieres editar: nombre, cedula o carrera: ")

# if editar == 'nombre':
#     nombre = input("ingrese el nuevo nombre: ")
#     contactos[0]['nombre'] = nombre

# elif editar == 'cedula':
#     cedula = int(input("ingrese la nueva cedula: "))
#     contactos[0]['cedula'] = cedula

# elif editar == 'carrera':
#     carrera = input("ingrese la nueva carrera: ")
#     contactos[0]['carrera'] = carrera

# print("se edito el campo seleccionado")

# for contacto in contactos:
#     print(f"NOMBRE DEL CONTACTO: {contacto['nombre']}")
#     print(f"CEDULA DEL CONTACTO: {contacto['cedula']}")
#     print(f"CARRERA DEL CONTACTO: {contacto['carrera']}")
