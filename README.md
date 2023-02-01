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
def preparar_cadena_Markov(palabras: dict, MAX_PAL: int, texto: list):
    cadena = {
        'START START': [],
        'START': [],
        'END': [],
        'END END': []
    }
    for linea in texto:
        for word in linea:
            # * GUARDAMOS LAS PALABRAS QUE INICIAN UNA FRASE
            if len(palabras[word]) == 0:
                if not word in cadena:
                    cadena['START START'].append(word)
            # * GUARDAMOS LAS PALABRAS QUE VAN DESPUÉS DE LAS QUE INICIAN LA FRASE
            elif len(palabras[word]) == 1:
                if not word in cadena:
                    cadena['START'].append(word)
            # * GUARDAMOS LA PALABRA QUE FINALIZA EL TEXTO
            elif word == linea[-1]:
                cadena['END END'].append(word)
            # * GUARDAMOS LAS PALABRAS QUE PUEDEN PRECEDER A LA PALABRA QUE FINALIZA EL TEXTO
            elif word == linea[-2]:
                cadena['END'].append(word)
            # * GUARDAMOS EL RESTO DE PALABRAS CUYO VALOR SERÁ LA PROBABILIDAD DE APARICIÓN DE CADA PALABRA
            else:
                if not word in cadena:
                    cadena[word] = 1/MAX_PAL
                else:
                    cadena[word] = ((cadena[word] * MAX_PAL) + 1)/MAX_PAL
    print(cadena)
    return cadena

def crear_frase(cadena: dict, palabras: dict):
    print()

def add_word(prev, next):
    frase = []
    frase[prev].append(next)
    return frase

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
        # * creamos almacens aleatorias
        crear_frase(preparar_cadena_Markov(palabras_dic, MAX_PAL, texto), palabras_dic)
        file.close()
    except Exception as e:
        print(e)
    finally:
        file.close()

~~~
