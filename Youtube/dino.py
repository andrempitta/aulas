import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint
from random import randrange

pygame.init()
pygame.mixer.init()

LARGURA = 640
ALTURA = 480

BRANCO = (255, 255, 255)

diretorio_princial = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_princial, 'dino/imagens')
diretorio_sons = os.path.join(diretorio_princial, 'dino/sons')

tela = pygame.display.set_mode((LARGURA, ALTURA)) 
pygame.display.set_caption('Dino')

sprite_sheep = pygame.image.load(os.path.join(diretorio_imagens, 'dinoSpritesheet.png')).convert_alpha()  # convert_aplha mantem a transparencia do desenho

colisao = pygame.mixer.Sound(os.path.join(diretorio_sons, 'death_sound.wav'))
colisao.set_volume(1)
colidiu = False

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons, 'jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.image_dinossouro = []
        for i in range(3):
            img = sprite_sheep.subsurface((i * 32, 0), (32, 32))
            img = pygame.transform.scale(img, (32 * 3, 32 * 3))
            self.image_dinossouro.append(img)
        self.index_lista = 0
        self.image = self.image_dinossouro[self.index_lista]
        self.rect = self.image.get_rect()  #  criando o retangule me volta da figura
        self.mask = pygame.mask.from_surface(self.image)
        self.pos_y_ini = ALTURA - 64 - 96//2
        self.rect.center = (100, ALTURA - 64)  # posicionando o centro do retangulo na posicao 100,100 da tela
        self.pulo = False

    def pular(self):
        self.pulo = True
        self.som_pulo.play()

    def update(self):
        if self.pulo == True:
            if self.rect.y < 200:
                self.pulo = False
            self.rect.y -= 20 
        else:
            if self.rect.y < self.pos_y_ini:
                self.rect.y += 20
            else:
                self.rect.y = self.pos_y_ini

        if self.index_lista > 2:  #  2 é o último desenho do dinosauor (que são três figuras no sheet)
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.image_dinossouro[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheep.subsurface((7 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)  # self.rect.center = (100, 100)
        self.rect.x = LARGURA - randrange(30, 300, 90)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 200, 50)  # self.rect.center = (100, 100)
            # self.rect.y = randint(50, 160)
        self.rect.x -= 10
          

class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheep.subsurface((6 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 64
        self.rect.x = pos_x * 64
        # self.rect.topright = (LARGURA, ALTURA - 75)

    def pos_hori(self, x):
        self.rect.x = x

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheep.subsurface((5 * 32, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (LARGURA , ALTURA - 64)
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA 
        self.rect.x -= 10


todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)
cacto = Cacto()
todas_as_sprites.add(cacto)

for i in range(LARGURA*2//64): #  gambiarra
    chao = Chao(i)
    todas_as_sprites.add(chao)

for i in range(4):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(BRANCO)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != dino.pos_y_ini:
                    pass
                else:
                    dino.pular()

    colisoes = pygame.sprite.spritecollide(dino, grupo_obstaculos, False, pygame.sprite.collide_mask)
    
    todas_as_sprites.draw(tela)

    if colisoes and colidiu == False:
        colisao.play()
        colidiu = True
        
    if colidiu == True:
        pass
    else:
        todas_as_sprites.update()



    pygame.display.flip()
