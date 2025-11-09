import pygame, random, sys

pygame.init()
pygame.mixer.init()

ANCHO, ALTO = 900, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Halloween Dulcero 🎃")

BLANCO = (255, 255, 255)
NARANJA = (255, 165, 0)
NEGRO = (0, 0, 0)
VERDE = (100, 200, 100)
AMARILLO = (255, 200, 0)
ROJO = (255, 100, 100)

fondo = pygame.image.load("assets/fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

jugador_img = pygame.image.load("assets/niño.png")
jugador_img = pygame.transform.scale(jugador_img, (100, 100))

fantasma_img = pygame.image.load("assets/fantasma.png")
fantasma_img = pygame.transform.scale(fantasma_img, (85, 85))

zombie_img = pygame.image.load("assets/zombie.png")
zombie_img = pygame.transform.scale(zombie_img, (90, 90))

dulces_imgs = [
    pygame.transform.scale(pygame.image.load("assets/sparkies.png"), (55, 55)),
    pygame.transform.scale(pygame.image.load("assets/chocorramo.png"), (55, 55)),
    pygame.transform.scale(pygame.image.load("assets/bubaloo.png"), (55, 55))
]
fuente = pygame.font.SysFont("Arial", 32)
fuente_titulo = pygame.font.SysFont("Arial", 48, bold=True)

sonido_zombie = pygame.mixer.Sound("assets/sonidozombie.mp3")
sonido_fantasma = pygame.mixer.Sound("assets/sonidofantasma.mp3")
sonido_dulce = pygame.mixer.Sound("assets/sonidodulce.mp3")

sonido_zombie.set_volume(0.7)
sonido_fantasma.set_volume(0.7)
sonido_dulce.set_volume(0.6)

def dibujar_boton(texto, x, y, w, h, color_fondo, color_texto):
    pygame.draw.rect(pantalla, color_fondo, (x, y, w, h), border_radius=10)
    texto_render = fuente.render(texto, True, color_texto)
    pantalla.blit(texto_render, (x + w/2 - texto_render.get_width()/2, y + h/2 - texto_render.get_height()/2))
    return pygame.Rect(x, y, w, h)

def menu_niveles():
    while True:
        pantalla.blit(fondo, (0, 0))
        titulo = fuente_titulo.render(" Elige el niveeeeeeeel ", True, BLANCO)
        pantalla.blit(titulo, (ANCHO/2 - titulo.get_width()/2, 100))

        boton_facil = dibujar_boton("Fácil", 300, 250, 300, 60, VERDE, NEGRO)
        boton_medio = dibujar_boton("Medio", 300, 330, 300, 60, AMARILLO, NEGRO)
        boton_dificil = dibujar_boton("Difícil", 300, 410, 300, 60, ROJO, NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_facil.collidepoint(event.pos):
                    return 1
                elif boton_medio.collidepoint(event.pos):
                    return 2
                elif boton_dificil.collidepoint(event.pos):
                    return 3

        pygame.display.flip()

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jugador_img
        self.rect = self.image.get_rect(center=(100, ALTO - 100))
        self.vel = 7

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.vel
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.vel
        if teclas[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.vel
        if teclas[pygame.K_DOWN] and self.rect.bottom < ALTO:
            self.rect.y += self.vel

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, imagen, velocidad):
        super().__init__()
        self.image = imagen
        self.rect = self.image.get_rect(center=(random.randint(ANCHO, ANCHO + 300), random.randint(50, ALTO - 50)))
        self.velocidad = velocidad

    def update(self):
        self.rect.x -= self.velocidad
        if self.rect.right < 0:
            self.rect.x = random.randint(ANCHO, ANCHO + 300)
            self.rect.y = random.randint(50, ALTO - 50)

class Dulce(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(dulces_imgs)
        self.rect = self.image.get_rect(center=(random.randint(50, ANCHO - 50), random.randint(50, ALTO - 50)))

def pantalla_final(puntos):
    while True:
        pantalla.blit(fondo, (0, 0))
        mensaje = fuente_titulo.render(f"¡Perdiste! Dulces: {puntos}", True, NARANJA)
        pantalla.blit(mensaje, (ANCHO/2 - mensaje.get_width()/2, 200))

        boton_reintentar = dibujar_boton("Volver a jugar", 300, 330, 300, 60, VERDE, NEGRO)
        boton_menu = dibujar_boton("Ir al menú", 300, 410, 300, 60, AMARILLO, NEGRO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_reintentar.collidepoint(event.pos):
                    return "reintentar"
                elif boton_menu.collidepoint(event.pos):
                    return "menu"

        pygame.display.flip()


def juego(nivel):
    jugador = Jugador()
    todos = pygame.sprite.Group()
    enemigos = pygame.sprite.Group()
    dulces = pygame.sprite.Group()

    todos.add(jugador)

    
    if nivel == 1:
        cantidad_enemigos = 2
        velocidad_enemigos = 2
    elif nivel == 2:
        cantidad_enemigos = 4
        velocidad_enemigos = 4
    else:
        cantidad_enemigos = 6
        velocidad_enemigos = 6

    for i in range(cantidad_enemigos):
        imagen = random.choice([fantasma_img, zombie_img])
        enemigo = Enemigo(imagen, velocidad_enemigos)
        enemigos.add(enemigo)
        todos.add(enemigo)

    for i in range(5):
        dulce = Dulce()
        dulces.add(dulce)
        todos.add(dulce)

    reloj = pygame.time.Clock()
    puntos = 0
    jugando = True

    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        jugador.update()
        enemigos.update()

        
        colision_dulce = pygame.sprite.spritecollide(jugador, dulces, True)
        for _ in colision_dulce:
            sonido_dulce.play()
            puntos += 1
            nuevo_dulce = Dulce()
            dulces.add(nuevo_dulce)
            todos.add(nuevo_dulce)

        
        enemigo_colision = pygame.sprite.spritecollideany(jugador, enemigos)
        if enemigo_colision:
            if enemigo_colision.image == zombie_img:
                sonido_zombie.play()
            else:
                sonido_fantasma.play()
            jugando = False

        pantalla.blit(fondo, (0, 0))
        todos.draw(pantalla)

        marcador = fuente.render(f"Dulces: {puntos}", True, BLANCO)
        pantalla.blit(marcador, (20, 20))

        pygame.display.flip()
        reloj.tick(60)

    return pantalla_final(puntos)

while True:
    nivel = menu_niveles()
    resultado = juego(nivel)
    if resultado == "menu":
        continue
    elif resultado == "reintentar":
        juego(nivel)
