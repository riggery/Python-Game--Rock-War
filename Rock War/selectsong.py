# -*- coding: utf-8 -*-
RESOLUTION = [800, 500]


import os
import os.path
from os.path import basename
import ntpath
ntpath.basename("a/b/c")
IMAGE_PATH = "image/"
SOUND_PATH="SOUND/"
MUSIC_PATH="songs/"
BUTTON_PATH = "image/"
#MUSIC_PATH = "C:\Users\RUI YANG\Desktop/112finalroject/try/UI/songs/"
#BUTTON_PATH = "C:\Users\RUI YANG\Desktop/112finalroject/try/UI/image/"
#FONT_PATH="C:\Users/RUI YANG/Desktop/112finalroject/try/UI/font/"
#IMAGE_PATH = "C:\Users\RUI YANG\Desktop/112finalroject/try/UI/image/"
import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
from math import sqrt
import ezmenu
import os
import os.path
from os.path import basename
import ntpath
ntpath.basename("a/b/c")

#from comb import Parallax, AnimatedSprite, runPiece
     
class Button(object):
    def __init__(self, image_filename, position):
        self.position = position
        self.image = pygame.image.load(image_filename)
    def render(self, surface):
        x, y = self.position
        w, h = self.image.get_size()
        x -= w / 2
        y -= h / 2
        surface.blit(self.image, (x, y))
 
    def is_over(self, point):
        point_x, point_y = point
        x, y = self.position
        w, h = self.image.get_size()
        x -= w /2
        y -= h / 2
        in_x = point_x >= x and point_x < x + w
        in_y = point_y >= y and point_y < y + h
        return in_x and in_y





class selectSong(object):
    def __init__(self):
     
        pygame.mixer.pre_init(44100, 16, 2, 1024*4)
        pygame.init()
        self.screen = pygame.display.set_mode((RESOLUTION[0],RESOLUTION[1]), 0)
        #font=pygame.font.Font("font\appleberry\appleberry.ttf",10)
        font=pygame.font.Font("font\urban_jungle\UrbanJungle.ttf",35)
        #font = pygame.font.SysFont("arial", 16)
        background = pygame.image.load("image/back4.jpg").convert()
        self.background = pygame.transform.scale(background, (RESOLUTION[0],RESOLUTION[1]))
        
        self.x=0
        x = 200
        y = 250
        #button_width =150
        self.buttons = {}
        self.buttons["prev"] = Button(BUTTON_PATH+"prev.png", (x, y))
        self.buttons["next"] = Button(BUTTON_PATH+"next.png", (x+400, y))
        #self.buttons["Back to Main Menu"] = Button(BUTTON_PATH+"next.png", (x+button_width*4, y+300))
        
     
        self.music_filenames = self.get_music(MUSIC_PATH)
        if len(self.music_filenames) == 0:
            print "No music files found in ", MUSIC_PATH
            return
     
        self.label_surfaces = []
        for filename in self.music_filenames:
            txt = os.path.split(filename)[-1]
            #print txt
            #print "Track:", txt
            txt = txt.split('.')[0].decode('gb2312')
            surface = font.render(txt, True, (204,204,51))
            self.label_surfaces.append(surface)
     
        self.current_track = 0
        self.max_tracks = len(self.music_filenames)
        pygame.mixer.music.load( self.music_filenames[self.current_track] )  
        
        self.clock = pygame.time.Clock()
        self.playing = True
        paused = False
        pygame.mixer.music.play()
        TRACK_END = USEREVENT + 1
        pygame.mixer.music.set_endevent(TRACK_END)
        self.ablum1=pygame.image.load(os.path.splitext(self.music_filenames[self.current_track])[0]+'.jpg').convert()
    
    def get_music(self,path):
        raw_filenames = os.listdir(path)
        music_files = []
        for filename in raw_filenames:
            if filename.lower().endswith('.ogg') or filename.lower().endswith('.mp3'):
                music_files.append(os.path.join(MUSIC_PATH, filename))
        return sorted(music_files)
    
    def path_leaf(self,path):
        head, tail = ntpath.split(path)
        return tail or ntpath.basename(head)
        
    
    def update(self,event):
            self.ablum1=pygame.image.load(os.path.splitext(self.music_filenames[self.current_track])[0]+'.jpg').convert()
           # print os.path.splitext(self.music_filenames[self.current_track])[0]+""
            if event.type == KEYDOWN and event.key==K_LEFT:
                self.current_track = (self.current_track + 1) % self.max_tracks
                pygame.mixer.music.load( self.music_filenames[self.current_track] )
                if self.playing:
                    pygame.mixer.music.play()
 
            #elif button_pressed == "prev":
            elif  event.type == KEYDOWN and event.key==K_RIGHT:
                if pygame.mixer.music.get_pos() > 3000:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play()
                else:
                    self.current_track = (self.current_track - 1) % self.max_tracks
                    pygame.mixer.music.load( self.music_filenames[self.current_track] )
                    if self.playing:
                        pygame.mixer.music.play()
            elif  event.type == KEYDOWN and event.key==K_RETURN:
                return 1
            elif event.type == KEYDOWN and event.key==K_ESCAPE:
                return 0
    
    def player(self):   
        self.screen.fill((0, 0, 255))
        self.screen.blit(self.background,(0,0))
        #print self.music_filenames[self.current_track]
        #print txt[self.current_track] 
        label = self.label_surfaces[self.current_track]
        #print label
        w, h = label.get_size()
        screen_w = RESOLUTION[0]
        self.screen.blit(label, ((screen_w - w)/2, 350))
    
        for self.button in self.buttons.values():
            self.button.render(self.screen)
        
        path=os.path.splitext(self.music_filenames[self.current_track])[0]   
 
        
        self.screen.blit(self.ablum1, (291,100))
        #self.screen.blit(self.ablumBlanket, (240,130))
        self.clock.tick(5)
        pygame.display.update()
        return self.path_leaf(path)
        
        
        


#
#playyy=selectSong()
#
#while True:
#    for event in pygame.event.get():
#        flag=playyy.update(event)
#        name=playyy.player()
#        print name
#        #print flag
#        
#if __name__ == "__main__":
# 
#    run()