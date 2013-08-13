import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import pygame, sys


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

###############################################################################
#Input before creat track
###############################################################################
RESOLUTION=[800,500]

class TrackGen(object):
  def __init__(self,question):
      self.screen = pygame.display.set_mode((RESOLUTION[0],RESOLUTION[1]))
      self.question=question
      self.name="fdsafd"
      self.current_string=[]

             
  def get_key(self):
    while 1:
      event = pygame.event.poll()
      if event.type == KEYDOWN:
        return event.key
      else:
        pass
  #
  def display_box(self, message):
    background = pygame.image.load("image/back5.jpg").convert()
    background = pygame.transform.scale(background, (800,500))
    self.screen.blit(background,(0,0))
    fontobject = pygame.font.Font(None,28)
    pygame.draw.rect(self.screen, (0,0,0),
                     ((self.screen.get_width() / 2) - 100,
                      (self.screen.get_height() / 2) - 10,
                      200,20), 0)
    pygame.draw.rect(self.screen, (242,255,27),
                     ((self.screen.get_width() / 2) - 202,
                      (self.screen.get_height() / 2) - 12,
                      404,24), 1)
   
    if len(message) != 0:
      self.screen.blit(fontobject.render(message, 1, (59,254,175)),
                  ((self.screen.get_width() / 2) - 200, (self.screen.get_height() / 2) - 10))
     
    pygame.display.flip()
  
  def update(self,event):
        pygame.font.init()
        self.display_box(self.question + ": " + string.join(self.current_string,""))
        inkey= self.get_key()
        if inkey == K_BACKSPACE:
          self.current_string =self.current_string[0:-1]
        elif inkey == K_RETURN:
          return 0
        elif inkey == K_ESCAPE:
          return 1
        elif inkey == K_MINUS:
          self.current_string.append("_")
        elif inkey <= 127:
          self.current_string.append(chr(inkey))
        #print  string.join(self.current_string,"")
        self.display_box(self.question + ": " + string.join(self.current_string,""))
        self.name=string.join(self.current_string,"")
    
  
  def ask(self,event):
    pygame.font.init()
   
    self.display_box(self.question + ": " + string.join(self.current_string,""))
    self.update(event)
    return self.name
  
  
  
  
  
  
  
  
  
#def run():
#  
#
#  trackname=TrackGen("Song Name")
#  while True:
#    event = pygame.event.poll()
#    if trackname.update(event)==0:
#       break
#    songname =trackname.ask(event)
#  print songname
#run()
