import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class calabaza(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('Jump_1.png'),
                                        util.cargar_imagen('Jump_2.png'),
                                        util.cargar_imagen('Jump_3.png'),
                                        util.cargar_imagen('Jump_4.png')]
        self.image = pygame.Surface([2, 1])
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(1, 2)
        self.velx = 2
        self.vel = (self.velx,3)
	self.estado = 1	
        
    def update(self,size):
        if self.estado == 1:
            teclas = pygame.key.get_pressed()
            if teclas[K_RIGHT]:
                self.velx = self.velx+ 2
                self.vel = (self.velx,3)
                print (self.velx)
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]

            if teclas[K_LEFT] and self.velx>2:
                self.velx -= 2
                self.vel = (self.velx,3)
                print (self.velx)
             
            """if self.rect.y < size[1] - 2:
                self.rect.y += self.vel[1]"""
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.cont]
        else:
            self.image = util.cargar_imagen("Dead (3).png") 
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect.size = (128,128)
        self.rect.y = size[1] - 128
            
