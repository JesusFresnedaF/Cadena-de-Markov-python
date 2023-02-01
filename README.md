# Cadena-de-Markov-python
~~~

import numpy as np
import random

#! Cadenas de Markov

# * Sustituimos signos de puntuación por espacios en blanco


def separar_signos(palabras):
    signos = [',', '.', ':', ';', '?', '¿', '!', '¡', '(', ')']
    for i in signos:
        palabras = palabras.replace(i, ' ')

    return palabras


# * Separamos el diccionario de palabras en un diccionario según el orden de aparición
def preparar_cadena_Markov(palabras: dict, MAX_PAL: int, texto: list):
    cadena = {
        'START START': [],
        'START': []
    }
    for word in palabras:
        if len(palabras[word]) == 0:
            if not word in cadena:
                cadena['START START'].append(word)
        elif len(palabras[word]) == 1:
            if not word in cadena:
                cadena['START'].append(word)
        else:
            if not word in cadena:
                cadena[word] = 1/MAX_PAL
            else:
                cadena[word] = ((cadena[word] * MAX_PAL) + 1) / MAX_PAL
    return cadena

def crear_frase(cadena: dict, linea: list, palabras: dict):
    frase = ""
    for state in cadena: 
        if state == 'START START':
            frase += random.choice(cadena[state])
        elif state == 'START':
            for word in palabras:
                print("cadena: ",cadena['START START'])
                print("palabras", palabras[word])
                # if cadena['START START'] in palabras[word]:
                    
    # print(frase)

# * MAIN
if __name__ == '__main__':
    lineas = []
    palabras = []
    texto = []
    palabras_dic = {}
    MAX_PAL = 0
    try:
        # * leemos lineas
        file = open("frases.txt", "rt")
        for linea in file:
            almacen = separar_signos(linea)
            palabras = almacen.rsplit()
            texto.append(palabras)
            for i in range(len(palabras)):
                MAX_PAL += 1
                # * todas las palabras detrás de esta palabra
                if not palabras[i] in palabras_dic:
                    palabras_dic[palabras[i]] = palabras[:i]
                else:
                    palabras_dic[palabras[i]].extend(palabras[:i])
        # * creamos lineas aleatorias
        for linea in texto:
            # print(linea)
            crear_frase(preparar_cadena_Markov(palabras_dic, MAX_PAL, texto), linea, palabras_dic)
    except Exception as e:
        print(e)
    finally:
        file.close()

~~~
