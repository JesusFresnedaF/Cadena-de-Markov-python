
import random

#! Cadenas de Markov

# * Sustituimos signos de puntuación por espacios en blanco
def separar_signos(palabras)->str:
    signos = [',', '.', ':', ';', '?', '¿', '!', '¡', '(', ')']
    for i in signos:
        palabras = palabras.replace(i, ' ')
    return palabras


# * Separamos el diccionario de palabras en un diccionario según el orden de aparición
def preparar_cadena_Markov(palabras: dict, texto: list):
    cadena = {
        'START START': [],
        'END': []
    }
    state = None
    # * Para cada linea del texto
    for linea in texto:
        # * añadimos la primera palabra de la linea
        cadena["START START"].append(linea[0])
        for i, word in enumerate(linea):
            # * si es la segunda palabra:
            if i == 1:
                # * si no existe ese estado lo creamos
                if not ("START"+" "+linea[i - 1]) in cadena:
                    cadena["START"+" "+ linea[i - 1]] = [word]
                # * si existe añadimos esa palabra al estado
                else:
                    cadena["START"+" "+ linea[i - 1]].append(word)
            # * si son el resto de palabras de la linea:
            if i > 1:
                # * si ese estado existe en el diccionario añadimos esa palabra
                if (linea[i-2]+" "+linea[i-1]) in cadena:
                    cadena[linea[i-2]+" "+linea[i-1]].append(word)
                # * si no existe creamos el estado con esa palabra
                else:
                    cadena[linea[i-2]+" "+linea[i-1]] = [word]
                # * guardamos el estado anterior
                state = linea[i-2]+" "+linea[i-1]
        # * por ultimo, añadimos el ultimo estado en 'END'
        cadena['END'].append(state)
    return cadena

# * Generamos una frase aleatoria según el diccionario de estados
def gen_frase(cadena:dict):
    state = 'START START'
    s = []
    frase = ""
    # * mientras que no lleguemos al estado final
    while not state in cadena['END']:
        # * guardamos una palabra aleatoria de ese estado
        word = random.choice(cadena[state])
        # * la añadimos a la frase
        frase += word + " "
        # * generamos el siguiente estado
        s = state.split(" ")
        state = s[1]+" "+word
    # * añadimos la palabra que corresponde a ese estado final
    frase += random.choice(cadena[state])
    frase+="."
    print(frase)

# * Leemos el texto y guardamos las palabras de cada linea en un diccionario
def leer_palabras(file):
    palabras = []
    texto = []
    palabras_dic = {}
    # * leemos las lineas del texto
    for linea in file:
        almacen = separar_signos(linea).lower()
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
        file = open("frases_informatica.txt", 'rt')
        palabras_dic, texto = leer_palabras(file)
        gen_frase(preparar_cadena_Markov(palabras_dic, texto))
    except Exception as e:
        print(e)
    finally:
        file.close()
