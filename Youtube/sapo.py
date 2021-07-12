import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
PRETO = (0, 0, 0)

clock = pygame.time.Clock()

tela = pygame.display.set_mode((largura, altura))  #  criar a tela
pygame.display.set_caption('sprites') #  nome da tela

class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Para inicialiar a Classe herdada
        self.sprites = []
        self.sprites.append(pygame.image.load('sapo/attack_1.png'))
        self.sprites.append(pygame.image.load('sapo/attack_2.png'))
        self.sprites.append(pygame.image.load('sapo/attack_3.png'))
        self.sprites.append(pygame.image.load('sapo/attack_4.png'))
        self.sprites.append(pygame.image.load('sapo/attack_5.png'))
        self.sprites.append(pygame.image.load('sapo/attack_6.png'))
        self.sprites.append(pygame.image.load('sapo/attack_7.png'))
        self.sprites.append(pygame.image.load('sapo/attack_8.png'))
        self.sprites.append(pygame.image.load('sapo/attack_9.png'))
        self.sprites.append(pygame.image.load('sapo/attack_10.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]  #  atributo herdado da classe 'pygame.sprite.Sprite'
        self.image = pygame.transform.scale(self.image, (128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False

    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual += self.atual + 1
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))


todas_as_sprites = pygame.sprite.Group()
sapo = Sapo()
todas_as_sprites.add(sapo)

while True:
    clock.tick(6)
    tela.fill(PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()


    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()  #  melhor (memória) que pygame.display.update()

