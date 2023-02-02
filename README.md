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
    cadena = {
        'START START': [],
    }
    for linea in texto:
        cadena["START START"].append(linea[0])
        for i, word in enumerate(linea):
            if i == 1:
                cadena["START"+" "+ linea[i - 1]] = [word]
                if not word in cadena["START"+" "+ linea[i - 1]]:
                    cadena["START"+" "+ linea[i - 1]].append(word)
            if i > 1:
                if word in cadena:
                    cadena[linea[i-2]+" "+linea[i-1]].append(word)
                else:
                    cadena[linea[i-2]+" "+linea[i-1]] = [word]
    print(cadena)

# def gen_frase(cadena:dict):
#     frase = " "
#     print(cadena)

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
    return palabras_dic, texto


# * MAIN
if __name__ == '__main__':
    texto = []
    palabras_dic = {}
    try:
        file = open("frases.txt", 'rt')
        palabras_dic, texto = leer_palabras(file)
        preparar_cadena_Markov(palabras_dic, texto)
        # gen_frase()
    except Exception as e:
        print(e)
    finally:
        file.close()

~~~
