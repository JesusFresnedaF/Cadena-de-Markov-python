# Cadena-de-Markov-python
~~~

import random

#! Cadenas de Markov

# * Sustituimos signos de puntuación por espacios en blanco
def separar_signos(palabras):
    signos = [',', '.', ':', ';', '?', '¿', '!', '¡', '(', ')']
    for i in signos:
        palabras = palabras.replace(i, ' ')
    return palabras


# * Separamos el diccionario de palabras en un diccionario según el orden de aparición
def preparar_cadena_Markov(palabras: dict, texto: list):
    for linea in texto:
        # print(linea)
        for i, word in enumerate(linea):
            if i == 0:
                add_word(("START","START"), word)
            elif i == 1:
                add_word(("START", linea[0]), word)
            else:
                add_word((linea[i - 2], linea[i - 1]), word)

def add_word(prev, next):
    almacen = {}
    almacen[prev].append(next)

# def crear_frase(cadena: dict, linea: list, palabras: dict):

# * leemos lineas
def leer_palabras(file):
    palabras = []
    texto = []
    palabras_dic = {}
    for linea in file:
        almacen = separar_signos(linea)
        palabras = almacen.rsplit()
        texto.append(palabras)
        for i in range(len(palabras)):
            # * todas las palabras después de esta palabra
            if not palabras[i] in palabras_dic:
                palabras_dic[palabras[i]] = palabras[i+1:]
            else:
                palabras_dic[palabras[i]].extend(palabras[i+1:])

    print(palabras_dic)
    return palabras_dic, texto


# * MAIN
if __name__ == '__main__':
    texto = []
    palabras_dic = {}
    try:
        file = open("frases.txt", 'rt')
        palabras_dic, texto = leer_palabras(file)
        # preparar_cadena_Markov(palabras_dic, texto)
    except Exception as e:
        print(e)
    finally:
        file.close()
      file.close()

~~~
