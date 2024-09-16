from pprint import pprint

string = "Hola mundo este es mi string"


def quita_espacios(texto):
    return [char for char in texto if char != " "]


def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


def ordena(dict):
    return sorted(dict.items(), key=lambda key: key[1], reverse=True)


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son : \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} : {valor} repeticiones\n"
    return mensaje


sin_espacios = quita_espacios(string)
contados = cuenta_caracteres(sin_espacios)
ordenados = ordena(contados)
mayores = mayores_tuplas(ordenados)
mensaje = crea_mensaje(mayores)

print(
    sin_espacios
)  # ['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o', 'e', 's', 't', 'e', 'e', 's', 'm', 'i', 's', 't', 'r', 'i', 'n', 'g']
pprint(
    contados, width=1
)  # {'H': 1, 'o': 3, 'l': 1, 'a': 1, 'm': 2, 'u': 1, 'n': 2, 'd': 1, 'e': 3, 's': 3, 't': 2, 'i': 2, 'r': 1, 'g': 1}

print(
    ordenados
)  # [('o', 3), ('e', 3), ('s', 3), ('m', 2), ('n', 2), ('t', 2), ('i', 2), ('H', 1), ('l', 1), ('a', 1), ('u', 1), ('d', 1), ('r', 1), ('g', 1)]
print(mayores)  # {'o': 3, 'e': 3, 's': 3}
print(
    mensaje
)  # Los que más se repiten son : \n- o : 3 repeticiones\n- e : 3 repeticiones\n- s : 3 repeticiones\n
