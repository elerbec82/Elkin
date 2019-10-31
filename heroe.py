import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('bird_0.png'),
                                        util.cargar_imagen('bird_1.png'),
                                        util.cargar_imagen('bird_2.png'),
                                        util.cargar_imagen('bird_3.png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 200)
        self.vel = (2,3)
		
        
    def update(self,size):
        teclas = pygame.key.get_pressed()
        if teclas[K_UP] and self.rect.y>=10:
            self.rect.y -= 10
        self.rect.x = (self.rect.x + self.vel[0]) % size[0]
        if self.rect.y < size[1] - 32:
            self.rect.y += self.vel[1]
        self.cont = (self.cont + 1) % 4
        self.image = self.imagenes[self.cont]
            
