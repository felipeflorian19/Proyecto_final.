from __future__ import print_function
import pygame
import random

VACIA = 0
MINA = 9
UNA = 1
DOS = 2
TRES = 3
CUATRO = 4
CINCO = 5

PERDIO = 0
GANO = 1
JUGANDO = 2

ANCHO = 640
ALTO = 640

BOMBA = ''


class Celda:
    def __init__(self, tipo=VACIA):
        self.tipo = tipo
        self.x = 0
        self.y = 0
        self.destapada = False


class Tablero:
    def __init__(self):
        self.n = 16
        self.m = 16
        self.matriz = []
        self.numero_minas = 40
        self.celdas_destapadas = 0

        self.inicializar_tablero()
        self.colocar_minas()
        self.computar_minas_vecinas()

    def inicializar_tablero(self):
        for i in range(self.n):
            fila = []
            for j in range(self.m):
                fila.append(Celda())
            self.matriz.append(fila)

    def colocar_minas(self):
        contador = 0

        while contador < self.numero_minas:
            i = random.randint(0, self.n - 1)
            j = random.randint(0, self.m - 1)

            if self.matriz[i][j].tipo == VACIA:
                self.matriz[i][j].tipo = MINA
                contador += 1

    def computar_minas_vecinas(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.matriz[i][j].tipo == VACIA:
                    tipo_celda_calculado = self.calcular_tipo(i, j)

                    if tipo_celda_calculado >= 3 and (i == 0 or i == self.n - 1 or j == 0 or j == self.m - 1):
                        self.matriz[i][j].tipo = DOS
                    else:
                        self.matriz[i][j].tipo = tipo_celda_calculado

    def calcular_tipo(self, i, j):
        contador_minas = 0

        if i - 1 >= 0:
            if self.matriz[i - 1][j].tipo == MINA:
                contador_minas += 1

        if i - 1 >= 0 and j + 1 < self.m:
            if self.matriz[i - 1][j + 1].tipo == MINA:
                contador_minas += 1

        if j + 1 < self.m:
            if self.matriz[i][j + 1].tipo == MINA:
                contador_minas += 1

        if i + 1 < self.n and j + 1 < self.m:
            if self.matriz[i + 1][j + 1].tipo == MINA:
                contador_minas += 1

        if i + 1 < self.n:
            if self.matriz[i + 1][j].tipo == MINA:
                contador_minas += 1

        if i + 1 < self.n and j - 1 >= 0:
            if self.matriz[i + 1][j - 1].tipo == MINA:
                contador_minas += 1

        if j - 1 >= 0:
            if self.matriz[i][j - 1].tipo == MINA:
                contador_minas += 1

        if i - 1 >= 0 and j - 1 >= 0:
            if self.matriz[i - 1][j - 1].tipo == MINA:
                contador_minas += 1

        return contador_minas

    def imprimir_tablero(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matriz[i][j].tipo, ' ', end='')
            print()


class Buscaminas:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = ANCHO, ALTO
        self.clock = pygame.time.Clock()
        self.tablero = Tablero()
        self.tablero.imprimir_tablero()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._display_surf.fill((255, 255, 255))
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def text_objects(self, text, font):
        text_surface = font.render(text, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def on_render(self):
        x = 0
        y = 0

        for i in range(self.tablero.n):
            x = 0
            for j in range(self.tablero.m):
                self.tablero.matriz[i][j].x = x
                self.tablero.matriz[i][j].y = y

                if self.tablero.matriz[i][j].destapada:
                    texto_pequehnio = pygame.font.SysFont("comicsansms", 20)
                    superficie_texto, rectangulo_texto = self.text_objects(str(self.tablero.matriz[i][j].tipo),
                                                                           texto_pequehnio)
                    rectangulo_texto.center = ((x + (40 / 2)), (y + (40 / 2)))
                    self._display_surf.blit(superficie_texto, rectangulo_texto)
                else:
                    pygame.draw.rect(self._display_surf, (140, 240, 130), (x, y, 40, 40), 3)
                x += 40
            y += 40

    def on_cleanup(self):
        pygame.quit()

    def gano(self):
        contador_celdas_destapadas = 0

        for i in range(self.tablero.n):
            for j in range(self.tablero.m):
                if self.tablero.matriz[i][j].destapada:
                    contador_celdas_destapadas += 1

        return contador_celdas_destapadas == (self.tablero.n * self.tablero.m - self.tablero.numero_minas)

    def destapar_celdas(self, i, j):

        if self.tablero.matriz[i][j].tipo == VACIA:
            self.tablero.matriz[i][j].destapada = True

        if i - 1 >= 0 and not self. tablero.matriz[i - 1][j].destapada:
            if self.tablero.matriz[i - 1][j].tipo != VACIA and self.tablero.matriz[i - 1][j].tipo != MINA:
                self.tablero.matriz[i - 1][j].destapada = True
            elif self.tablero.matriz[i - 1][j].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i - 1, j)

        if i - 1 >= 0 and j + 1 < self.tablero.m and not self.tablero.matriz[i - 1][j + 1].destapada:
            if self.tablero.matriz[i - 1][j + 1].tipo != VACIA and self.tablero.matriz[i - 1][j + 1].tipo != MINA:
                self.tablero.matriz[i - 1][j + 1].destapada = True
            elif self.tablero.matriz[i - 1][j + 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i - 1, j + 1)

        if j + 1 < self.tablero.m and not self.tablero.matriz[i][j + 1].destapada:
            if self.tablero.matriz[i][j + 1].tipo != VACIA and self.tablero.matriz[i][j + 1].tipo != MINA:
                self.tablero.matriz[i][j + 1].destapada = True
            elif self.tablero.matriz[i][j + 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i, j + 1)

        if i + 1 < self.tablero.n and j + 1 < self.tablero.m and not self.tablero.matriz[i + 1][j + 1].destapada:
            if self.tablero.matriz[i + 1][j + 1].tipo != VACIA and self.tablero.matriz[i + 1][j + 1].tipo != MINA:
                self.tablero.matriz[i + 1][j + 1].destapada = True
            elif self.tablero.matriz[i + 1][j + 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i + 1, j + 1)

        if i + 1 < self.tablero.m and not self.tablero.matriz[i + 1][j].destapada:
            if self.tablero.matriz[i + 1][j].tipo != VACIA and self.tablero.matriz[i + 1][j].tipo != MINA:
                self.tablero.matriz[i + 1][j].destapada = True
            elif self.tablero.matriz[i + 1][j].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i + 1, j)

        if i + 1 < self.tablero.n and j - 1 >= 0 and not self.tablero.matriz[i + 1][j - 1].destapada:
            if self.tablero.matriz[i + 1][j - 1].tipo != VACIA and self.tablero.matriz[i + 1][j - 1].tipo != MINA:
                self.tablero.matriz[i + 1][j - 1].destapada = True
            elif self.tablero.matriz[i + 1][j - 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i + 1, j - 1)

        if j - 1 >= 0 and not self.tablero.matriz[i][j - 1].destapada:
            if self.tablero.matriz[i][j - 1].tipo != VACIA and self.tablero.matriz[i][j - 1].tipo != MINA:
                self.tablero.matriz[i][j - 1].destapada = True
            elif self.tablero.matriz[i][j - 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i, j - 1)

        if i - 1 >= 0 and j - 1 >= 0 and not self.tablero.matriz[i - 1][j - 1].destapada:
            if self.tablero.matriz[i - 1][j - 1].tipo != VACIA and self.tablero.matriz[i - 1][j - 1].tipo != MINA:
                self.tablero.matriz[i - 1][j - 1].destapada = True
            elif self.tablero.matriz[i - 1][j - 1].tipo == VACIA:
                self.tablero.matriz[i][j].destapada = True
                self.destapar_celdas(i - 1, j - 1)

    def mostrar_bombas(self):
        for i in range(self.tablero.n):
            for j in range(self.tablero.m):
                if self.tablero.matriz[i][j].tipo == MINA:
                    self._display_surf.blit(pygame.image.load('bomba.png'), (i * 40, j * 40))

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        estado_juego = True

        while self._running:
            event = pygame.event.poll()

            for event in pygame.event.get():
                self.on_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and estado_juego:
                posicion = event.pos
                y = posicion[0] / 40
                x = posicion[1] / 40
                if not self.tablero.matriz[x][y].destapada:
                    if self.tablero.matriz[x][y].tipo == MINA:
                        self.tablero.matriz[x][y].destapada = True
                        self.tablero.matriz[x][y].tipo = BOMBA
                        self.mostrar_bombas()
                        estado_juego = False
                        continue
                    elif VACIA < self.tablero.matriz[x][y].tipo <= CINCO:
                        self.tablero.matriz[x][y].destapada = True
                    else:
                        self.destapar_celdas(x, y)

                estado_juego = not self.gano()

            if not estado_juego:
                texto_pequehnio = pygame.font.SysFont("comicsansms", 40)
                estado_juego = self.gano()
                superficie_texto, rectangulo_texto = self.text_objects('Gano' if estado_juego else 'Perdio',
                                                                       texto_pequehnio)
                rectangulo_texto.center = ((ANCHO / 2), (ALTO / 2))
                self._display_surf.blit(superficie_texto, rectangulo_texto)

                estado_juego = False

            self.on_loop()
            self.on_render()
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    theApp = Buscaminas()
    theApp.on_execute()
