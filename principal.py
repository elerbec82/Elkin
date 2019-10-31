import sys, pygame, util
from pygame.locals import *
from calabaza import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def game():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Flappy" )
    background_image = util.cargar_imagen('fondo.jpg');
    obstaculo_image = util.cargar_imagen('piedra.jpg');
    obstaculo_image = pygame.transform.scale(obstaculo_image, (64,64))
    obstaculo_rect = obstaculo_image.get_rect()
    obstaculo_rect.move_ip(SCREEN_WIDTH/2,SCREEN_HEIGHT - 64)
    pygame.mouse.set_visible( False )
    heroe = calabaza()
    
    while True:       
        heroe.update((SCREEN_WIDTH,SCREEN_HEIGHT))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(obstaculo_image, (SCREEN_WIDTH/2,SCREEN_HEIGHT - 64))
        screen.blit(heroe.image, heroe.rect)
        if heroe.rect.colliderect(obstaculo_rect):
            heroe.estado = 0
            
        pygame.display.update()
        pygame.time.delay(50)

      
if __name__ == '__main__':
      game()

