######################################
#main menu
######################################
import os
import sys
import pygame
from pygame.locals import *
from random import randint
from gameobjects.vector2 import Vector2
import cv2
import pygame.midi
import pygame.mixer
from pygame.locals import *
from sys import exit
import ezmenu
import time

from selectsong import *
from visioncrl import visionPart
from maingame import *
from inputbox import *
from createTrack import *
from score import *


import os
import os.path
from os.path import basename
import ntpath
ntpath.basename("a/b/c")
IMAGE_PATH = "image/"
SOUND_PATH="SOUND/"
MUSIC_PATH="songs/"
#IMAGE_PATH = "C:\Users\RUI YANG\Desktop/112finalroject/try/UI/image/"
#SOUND_PATH="C:\Users\RUI YANG\Desktop/112finalroject/try/UI/SOUND/"
#MUSIC_PATH="C:\Users\RUI YANG\Desktop/112finalroject/try/UI/songs/"





class StructUI(object):
    def __init__(self):
        self.RESOLUTION = (800,500)
        ####### menu flag initalize #######
        self.main_menu_flag = True
        self.newgame_flag = False
        self.selectsong_flag=False
        self.create_flag=False
        self.inputname_flag=False
        self.option_menu_flag = False
        self.testdevice_flag=False
        self.achievement_flag=False
        self.currentsong=["Send Him Away"]
        self.clock = pygame.time.Clock()
        
        self.score=0
        self.accuracy=0
        
        pygame.init()
        pygame.display.set_caption("Rock War")
        self.screen = pygame.display.set_mode((800,500))
        self.main_song = "SOUND/menu.ogg"
        background = pygame.image.load("image/back3.jpg").convert()
        self.background = pygame.transform.scale(background, (800,500))
        pygame.mixer.music.load(self.main_song)
        pygame.mixer.music.play(-1)
        self.controlstate=1
        self.storename=[""]
        self.recordstate=-1
        #saat = pygame.time.Clock()

    def newGame(self):
        print "tttttttttttttttttttttttthere"
        self.newgame_flag = True
        self.main_menu_flag =False
        self.selectsong_flag=False
        self.option_menu_flag = False
        self.testdevice_flag=False
        pygame.key.set_repeat()
        self.clock = pygame.time.Clock()
        #self.controlstate=1
        self.game=runPiece(self.currentsong[0])
        flag_key=[0,0,0,0,0]
        self.enterGame=MainGame(self.controlstate,self.currentsong[0])
        pygame.mixer.music.play()

    def testDevice(self):
        self.test=visionPart(1)
        self.testdevice_flag=True
    
    def achievement(self):
        self.main_menu_flag = False
        self.newgame_flag = False
        self.selectsong_flag=False
        self.create_flag=False
        self.inputname_flag=False
        self.option_menu_flag = False
        self.testdevice_flag=False
        self.achievement_flag=True
        self.achieve=Score("hero",self.score,self.accuracy)
        self.achieve.loadmusic()
        
    
    def selectList(self):
        self.newgame_flag =False
        self.main_menu_flag =False
        self.selectsong_flag=True
        self.option_menu_flag = False
        self.testdevice_flag=False
        self.achievement_flag=False
        self.songlist=selectSong()

    def createTrack(self):
        self.main_menu_flag = False
        self.newgame_flag = False
        self.selectsong_flag=False
        self.create_flag=True
        self.achievement_flag=False
        self.inputname_flag=False
        self.option_menu_flag = False
        self.testdevice_flag=False
        self.recordstate=0
        if(self.storename[0]!=""):
            self.compose=writeTrack(self.storename[0])
            if self.compose.loadmusic()==0:
                self.inputTrackName()
           # else:
                #continue
                
        else:
            self.inputTrackName()
    
    def inputTrackName(self):
        self.main_menu_flag = False
        self.newgame_flag = False
        self.selectsong_flag=False
        self.achievement_flag=False
        self.create_flag=False
        self.inputname_flag=True
        self.testdevice_flag=False
        self.trackname=TrackGen("Song Name")
    
    def event_handler(self,event):
        if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                   # pygame.mixer.music.set_volume(1.0)
                    self.backmain()
                    #self.main_menu_flag = True
                    #self.newgame_flag = False
                    #self.selectsong_flag = False
                    #self.testdevice_flag=False
                    #self.achievement_flag=False
                    #pygame.mixer.music.load(self.main_song)
                    #pygame.mixer.music.play(-1)
                elif event.key == K_0:
                    pygame.mixer.music.set_volume(1.0)
                    self.achievement()
                    pygame.mixer.music.load(self.main_song)
                    pygame.mixer.music.play(-1)
                elif event.key == K_p:
                        self.pause=True
                        #pygame.time.delay(100)
                        #pygame.mixer.music.pause()
                elif event.key == K_s:
                        self.pause=False
                        #pygame.mixer.music.unpause()
                        #continue
                        #pass

    
        if event.type == QUIT:
            return
        
    def vcontrol(self):
        self.controlstate=0

    def options(self):
        self.newgame_flag =False
        self.main_menu_flag =False
        self.selectsong_flag=False
        self.option_menu_flag = True
        self.testdevice_flag=False
        
    
    def backmain(self):
        self.newgame_flag =False
        self.main_menu_flag =True
        self.selectsong_flag=False
        self.option_menu_flag = False
        self.testdevice_flag=False
        self.achievement_flag=False
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load(self.main_song)
        pygame.mixer.music.play(-1)
        
    
    def keycontrol(self):    
         self.controlstate=1
    def quitGame(self):
        pygame.quit()
        sys.exit()
        
    def run(self):        
        pygame.key.set_repeat()
        #clock = pygame.time.Clock()
        self.pause=False
        main_menu = ezmenu.EzMenu(
            ["Quick Play", self.newGame],
            ["Select Song",self.selectList],
            ["Create Track", self.inputTrackName],  
            ["Options", self.options],
            ["Quit Game", self.quitGame])
        main_menu.center_at(240, 300)
        main_menu.set_font(pygame.font.Font("font\urban_jungle\UrbanJungle.ttf", 35))
        main_menu.set_highlight_color((204,153,51))
        main_menu.set_normal_color((102,51,0))
        
        
        option_menu = ezmenu.EzMenu(
            ["Device Test",self.testDevice],
            ["Vision Control",self.vcontrol],
            ["Keyboard Control", self.keycontrol],
            ["Back", self.backmain])
        option_menu.center_at(240, 300)   
        option_menu.set_font(pygame.font.Font("font\urban_jungle\UrbanJungle.ttf", 40))
        option_menu.set_highlight_color((204,153,51))
        option_menu.set_normal_color((102,51,0))

        
        while True:
         self.screen.fill((0, 0, 255))
         self.screen.blit(self.background,(0,0))
         
         if self.newgame_flag == True:
            print "here"
            for event in pygame.event.get():
                self.event_handler(event)
                if event.type == pygame.QUIT:
                      pygame.quit()
                      return
                self.enterGame.update(self.game,event)
            self.score,self.accuracy=self.enterGame.runMainGame(self.game,self.clock,self.controlstate)
            #self.score,self.accuracy=self.enterGame.runMainGame(self.game,self.controlstate)
            
         elif self.testdevice_flag == True:
            pygame.mixer.music.set_volume(0.0)
            self.test.visonInWhile()
            for event in pygame.event.get():
                self.event_handler(event)
                print "vision"
         else:
            for event in pygame.event.get():
               self.event_handler(event)
               if event.type == pygame.QUIT:
                      pygame.quit()
                      return
                   
               if self.main_menu_flag == True:
                   self.newgame_flag =False
                   #self.screen.fill((0, 0, 255))
                   
                   self.screen.blit(self.background,(0,0))
                   main_menu.durum = False
                   #main_menu.update(events)
                   main_menu.update(event)
                   main_menu.draw(self.screen)      
           
               elif self.option_menu_flag == True:
                   main_menu.durum = True
                   option_menu.durum = False
                   self.screen.fill((0, 0, 255))
                   self.screen.blit(self.background,(0,0))
                   option_menu.draw(self.screen)
                   option_menu.update(event)
                   #pygame.display.flip()           
               #elif self.newgame_flag == True:
               #    self.enterGame.update(self.game,event)
               #    self.enterGame.runMainGame(self.game,clock,self.controlstate)
               elif self.selectsong_flag == True:
                    if self.songlist.update(event)==1:
                        self.newGame()
                    else:
                        self.currentsong[0]=self.songlist.player()
                    #print  self.currentsong[0]
               elif self.inputname_flag == True:
                  #event = pygame.event.poll()
                   if self.trackname.update(event)==0:
                      self.storename[0]=self.trackname.ask(event)
                      self.createTrack()
                   elif self.trackname.update(event)==1:
                       self.backmain()
                      
                   #self.trackname.ask(event)
                   #self.storename[0] =self.trackname.ask(event)
               #self.storename[0]=name
               
               elif self.create_flag==True:
                   self.compose.display(self.clock)
                   if self.compose.update(event,self.clock)==0:
                      #self.compose.file.close()
                      self.backmain()
                   self.clock.tick(60)
                      
               elif self.achievement_flag==True:
                  self.achieve.display()
                  self.achieve.update(event,self.clock)
                
                      
                      
                      #  self.recordstate=1
         #pygame.display.flip()               
         #if self.recordstate==0:
         #           break
         #          #self.compose.update(event,clock)
         #              
         #          #clock.tick(60)
         
                        
               pygame.display.flip()






run= StructUI()


if __name__ == "__main__":
         run.run()


