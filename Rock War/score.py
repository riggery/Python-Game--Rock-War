import pygame, sys
from pygame.locals import *
from font import *
from maingame import load_sliced_sprites

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

class Score(object):
	def __init__(self,filename,score,accuracy):
		pygame.init()
		self.screen = pygame.display.set_mode((800,500))
		background = pygame.image.load(str(IMAGE_PATH)+"scoreback.png").convert()
		self.background = pygame.transform.scale(background, (800,500))
		fontobject = pygame.font.Font(None,28)
		pygame.mixer.pre_init(44100,-16,2, 1024)
		pygame.mixer.init()
		self.font_preferences = [
                        "Bizarre-Ass Font Sans Serif",
                        "They definitely dont have this installed Gothic",
                        "Papyrus",
                        "Comic Sans MS"]
		self.loop = 1
		self.filename=filename
                self.score=score
                self.accuracy=accuracy
                self.text = create_text("Score         "+str(self.score), self.font_preferences, 30, (0, 128, 0))
                self.textAcc = create_text("Accuracy   ", self.font_preferences, 30, (0, 128, 0))
                self.star = load_sliced_sprites(251, 50, str(IMAGE_PATH)+'star.png')
                #text = create_text("SCORE   "+str(game.scoreNum*85), self.font_preferences, 30, (0, 128, 0))
                #textAcc = create_text("ACCURACY   "+str(game.accuracy*100), self.font_preferences, 30, (0, 128, 0))

	
	def display(self):
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()
                self.screen.blit(self.text,
                    (200, 150+self.text.get_height() // 2))
                self.screen.blit(self.textAcc,
                    (200, 200+self.text.get_height() // 2))
                if self.accuracy==0:
                    self.screen.blit(self.star[0],(250,280))
                elif 30>self.accuracy>0:
                    self.screen.blit(self.star[1],(250,280))
                elif 60>self.accuracy>=30:
                    self.screen.blit(self.star[2],(250,280))
                elif 80>self.accuracy>=60:
                    self.screen.blit(self.star[3],(250,280))
                elif 95>self.accuracy>=80:
                    self.screen.blit(self.star[4],(250,280))
                elif self.accuracy>=95:
                    self.screen.blit(self.star[5],(250,280))
	        pygame.display.flip()
                
	def loadmusic(self):
		try:
		        pygame.mixer.music.load(str(self.filename)+'.ogg')
		except:
		        return 0
		else:
			self.file = open(str(self.filename)+'.txt',"w")
			pygame.mixer.music.play()
	
	def update(self,event,clock):	
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				return 0
			
#			
#achieve=Score("hero",1893,67)
#achieve.loadmusic()
#clock = pygame.time.Clock()
#while True:
#	for event in pygame.event.get():
#	       achieve.display()
#               if achieve.update(event,clock)==0:
#		  achieve.loop = 0
#	if achieve.loop==0:
#		break
#		#  print "break"
#       
#       	clock.tick(60)