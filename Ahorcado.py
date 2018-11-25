import time
import random


CATEGORIAS = ['tecnologia', 'animales', 'paises', 'nombres', 'peliculas' ]
palabras = []


def mostrar_categorias():
    for i in range(len(CATEGORIAS)):
        print('{}. {}'.format(i + 1, CATEGORIAS[i].capitalize()))
    print('0. Salir')

def cargar_palabras(categoria):
    with open('{}.txt'.format(categoria)) as archivo:
        for palabra in archivo:
            palabras.append(palabra.replace('\n', ''))

def continuar_jugando():
    print('¿Desea continuar jugando?')
    print('1. Sí')
    print('2. No')
    opcion = int(input('Seleccione opción: '))

    return True if opcion == 1 else False


def main():
    nombre = input("Ingrese su nombre jugador :")
    print(" ")

    continua = True

    while continua:
        mostrar_categorias()
        categoria = int(input('Seleccione categoria (0 para salir): '))
        if (categoria != 0):
            categoria -= 1

            cargar_palabras(CATEGORIAS[categoria])

            print("hola," + nombre + " " "vamos a empezar a jugar!")
            time.sleep(1)
            print(" ")
            print("te daremos la palabra que tienes que adivinar")

            palabra = random.choice(palabras)

            letra_del_jugador = ' '

            vidas = 7
            while vidas > 0:

                intentos_fallidos = 0
                for letra_esogida in palabra:
                    if letra_esogida in letra_del_jugador:
                        print(letra_esogida, end=" ")
                    else:
                        print("x", end=" ")
                        intentos_fallidos += 1

                if intentos_fallidos == 0:
                    print("BIEN, Ganaste :D")
                    break
                letra_que_quiere = input("ingrese alguna letra: ")
                letra_del_jugador += letra_que_quiere

                if letra_que_quiere not in palabra:
                    vidas -= 1
                    print("lo siento esa letra no era")
                    print("te quedan ", + vidas, " vidas ")
                    ab = ["+__+   ""\n"" | |""\n", "O""\n", "  |""\n", "  |""\n", "  |""\n", " |""\n", " ========"]
                    ac = ["+__+" "\n""| | ""\n" "O ""\n""| ""\n""  |""\n""  | ""\n""  |""\n""  | ""\n" " ========"]
                    ad = ["+__+""\n", " | |""\n", " O ""\n", "/| ""\n", "   |""\n", "   |""\n", "   |""\n", "========"]
                    ae = ["+__+""\n", " | |""\n", " O ""\n", "/|\ ""\n", "   |""\n", "   |""\n", "   |""\n", "========"]
                    af = ["+__+""\n", " | |""\n", " O ""\n", "/|\ ""\n", "/""\n", "   |""\n", "   |""\n", "   |""\n",
                          "========"]
                    ah = [" +__+""\n", " | |""\n", " O""\n", "/|\|""\n", "/ \|""\n", "   |""\n", "========="]
                    if vidas == 6:
                        a = " ".join(ab)
                        print(a)

                    elif vidas == 5:
                        b = " ".join(ac)
                        print(b)
                    elif vidas == 4:
                        c = " ".join(ad)
                        print(c)
                    elif vidas == 3:
                        d = " ".join(ae)
                        print(d)
                    elif vidas == 2:
                        e = "  ".join(af)
                        print(e)
                    elif vidas == 1:
                        f = " ".join(ah)
                        print(f)
                if vidas == 0:
                    print("perdiste, sera a la proxima ")
            else:
                print(" gracias por jugar ")

            continua = continuar_jugando()

        else:
            break


if __name__ == '__main__':
    main()
    print('El juego terminó')
