import pygame
import sys
from pygame.locals import *
import os 


def events():
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
         pygame.quit()
         sys.exit()


def main():
 W,H =576,1024
 HW,HH=W/2,H/2
 AREA=W*H

 pygame.init()
 CLOCK=pygame.time.Clock()
 DS= pygame.display.set_mode((W,H))
 pygame.display.set_caption("Background Scrolling")
 bkgd=pygame.image.load("images/game-background-7980_imgs_7980_4.jpg").convert()
 bird=pygame.image.load("images/twitter_bird_flying.png")
 x=0
 while True:
    events()
    rel_x=x%bkgd.get_rect().width
    x-=1
    DS.blit(bkgd,(rel_x-bkgd.get_rect().width,0))
    if rel_x<W:
        DS.blit(bkgd,(rel_x,0))

    pygame.display.update()
    CLOCK.tick(500)
    
    

    DS.blit(bird,(0,0))
    pygame.display.update()

if __name__ == '__main__':
    main()

