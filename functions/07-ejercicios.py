def es_palindromo(palabra):
    palabra = palabra.replace(
        " ", ""
    ).lower()  # Elimina espacios y convierte a minúsculas
    return palabra == palabra[::-1]  # Compara la palabra con su inversa


print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola Mundo"))
