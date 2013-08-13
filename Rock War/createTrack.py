import pygame, sys
from pygame.locals import *
from font import *



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

class writeTrack(object):
	def __init__(self,filename):
		pygame.init()
		self.screen = pygame.display.set_mode((800,500))
		background = pygame.image.load(str(IMAGE_PATH)+"record.jpg").convert()
		self.background = pygame.transform.scale(background, (800,500))
		fontobject = pygame.font.Font(None,28)
		pygame.mixer.pre_init(44100,-16,2, 1024)
		pygame.mixer.init()
		self.loop = 1
		self.filename=filename
		self.font_preferences = [
			"Bizarre-Ass Font Sans Serif",
			"They definitely dont have this installed Gothic",
			"Papyrus",
			"Comic Sans MS"]
                self.textA = create_text(" ", self.font_preferences, 52, (255, 255, 255))
		self.textB = create_text(" ", self.font_preferences, 52, (139, 128, 0))
		self.textC = create_text(" ", self.font_preferences, 52, (139, 128, 0))
		self.textD = create_text(" ", self.font_preferences, 52, (139, 128, 0))
		self.textE = create_text(" ", self.font_preferences, 52, (139, 128, 0))
		

	def display(self,clock):
		left=241
		space=62
		height=227
		self.screen.blit(self.background,(0,0))
		self.screen.blit(self.textA,(left,height))
		self.screen.blit(self.textB,(left+space, height))
		self.screen.blit(self.textC,(left+space*2,height))
		self.screen.blit(self.textD,(left+space*3-10, height))
		self.screen.blit(self.textE,(left+space*4-10, height))
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
				self.file.close()
				return 0
			if event.key == K_1:
				self.file.write("10000\n")
				print "A"
				self.textA = create_text("A", self.font_preferences, 40, (255, 255, 255))
				
			if event.key == K_2:
				self.file.write("01000\n")
				print "B"
				self.textB = create_text("B", self.font_preferences, 40, (255, 255, 255))
			if event.key == K_3:
				self.file.write("00100\n")
				print "C"
				self.textC = create_text("C", self.font_preferences, 40, (255, 255, 255))
			if event.key == K_4:
				self.file.write("00010\n")
				print "D"
				self.textD = create_text("D", self.font_preferences, 40, (255, 255, 255))
			if event.key == K_5:
				self.file.write("00001\n")
				print "E"
				self.textE = create_text("E", self.font_preferences, 40, (255, 255, 255))
	        else:
			self.file.write("00000\n")
			self.textA = create_text(" ", self.font_preferences, 52, (0, 128, 0))
			self.textB = create_text(" ", self.font_preferences, 52, (0, 128, 0))
			self.textC = create_text(" ", self.font_preferences, 52, (0, 128, 0))
			self.textD = create_text(" ", self.font_preferences, 52, (0, 128, 0))
			self.textE = create_text(" ", self.font_preferences, 52, (0, 128, 0))
##			
#compose=writeTrack("hero")
#compose.loadmusic()
#Y=0
#clock = pygame.time.Clock()
#while True:
#	for event in pygame.event.get():
#	       compose.display(clock)
#               if compose.update(event,clock)==0:
#		  compose.loop = 0
#	pygame.display.flip()     
#	if compose.loop==0:
#		break
#
#       
#       	clock.tick(60)