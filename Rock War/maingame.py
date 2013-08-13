import os 
import pygame
from pygame.locals import *
from random import randint
from gameobjects.vector2 import Vector2
import cv2
import pygame.midi
import pygame.mixer
from pygame.locals import *
from sys import exit


from visioncrl import visionPart
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

class Score(object):
    def __init__(self,song):
        self.stuff=[]
        self.beat=0
        #self.x = 52
        self.space=RESOLUTION[0]/10+5
        self.x =RESOLUTION[1]/4
        self.color = 0
        self.score=[]
        self.song=song
        #a = open('Send Him Away.txt',"r")
        #a = open('hero.txt',"r")
        a = open(str(MUSIC_PATH)+self.song+".txt")
        a = a.readlines()
        self.y = -len(a)*69
 
    def readRythm(self):
         #scoreFile = open('Send Him Away.txt',"r")
         #scoreFile = open('hero.txt',"r")
         scoreFile = open(str(MUSIC_PATH)+self.song+".txt")
         for line in scoreFile:
             for m in line:
                self.score.append(m)
         return self.score
    
    def translateRythm(self):
        while self.beat< len(self.score):
             if self.score[self.beat] == '\n':               #newnline
                     self.y += 69
                     self.x = RESOLUTION[1]/4
                     self.color = 0
             elif self.score[self.beat] == '0':              #no draw  skip it
                     #self.x += 76
                     self.x += self.space
                     self.color += 1
             elif self.score[self.beat] == '1':              #call draw beat
                     #self.x  += 76
                     self.x += self.space
                     self.color += 1
                     self.stuff.append((self.x,self.y,self.color))
             self.beat+= 1
        return self.stuff

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, images, fps = 10):
        pygame.sprite.Sprite.__init__(self)
        # Animation 
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        self._images = images
        self.image = self._images[self._frame]
        # Movement
        self.location = Vector2(0,0)
        self.destination = Vector2(0,0)
        self.heading = None
        #self.speed = 0.                       
    def process(self, t):
        if self.speed > 0. and self.location != self.destination:
                destination = self.destination - self.location				
                distance = destination.get_length()
                self.heading = destination.get_normalized()
                most_accurate_distance 	= min(distance, t*self.speed)
                self.location += most_accurate_distance*self.heading
                            
    def update(self, t):
        if t - self._last_update > self._delay:
                self._frame += 1
                if self._frame >= len(self._images):
                        self._frame = 0
                        
                self.image = self._images[self._frame]
                self._last_update = t
    
    def render(self, screen):
        screen.blit(self.image, self.location)



class FallingPiece(AnimatedSprite):
    def __init__(self, images, fps = 60):
        AnimatedSprite.__init__(self, images, fps)
        self.speed = 390.
        #self.speed = 100.
        self.default_speed = self.speed
        #self.location =Vector2(100, RESOLUTION[1]/2)
        #self.location =Vector2()
        #self.destination = self.location
        self.label=-1
        self.keyflag=0
        self.image = self._images[0]

    def update(self, t):
        self.speed = self.default_speed

def load_sliced_sprites(w, h, filename):
    images = []
    master_image = pygame.image.load(os.path.join('', filename)).convert_alpha()
    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_height/h)):
    	images.append(master_image.subsurface((0,i*h,w,h)))
    return images

class runPiece(FallingPiece):
    def __init__(self,song):
        self.flag_key=[0,0,0,0,0]
        self.scoreNum=0
        self.countDown=0
        self.accuracy=0
        self.endflag=0
        self.song=song
        self.totalnote=0
        self.elements= []
	self.key_A_images = load_sliced_sprites(86, 50, str(IMAGE_PATH)+'key_A.png')
	self.key_B_images = load_sliced_sprites(86, 50, str(IMAGE_PATH)+'key_B.png')
	self.key_C_images = load_sliced_sprites(86, 50, str(IMAGE_PATH)+'key_C.png')
	self.key_D_images = load_sliced_sprites(86, 50, str(IMAGE_PATH)+'key_D.png')
	self.key_E_images = load_sliced_sprites(86, 50, str(IMAGE_PATH)+'key_E.png')
        self.fire_images = load_sliced_sprites(86, 164/2, str(IMAGE_PATH)+'fire.png')
	self.piece_A_images = load_sliced_sprites(60,261/7,str(IMAGE_PATH)+'pieceA.png')
        self.light_images = load_sliced_sprites(600,2000/2,str(IMAGE_PATH)+'light.png')
        self.lightright_images = load_sliced_sprites(600,2000/2,str(IMAGE_PATH)+'lightright.png')
        
        self.fail = pygame.mixer.Sound(str(SOUND_PATH)+"playError.wav")
        
        
        self.space=RESOLUTION[0]/10
        self.left_space=RESOLUTION[1]/4
        self.key_position_y=RESOLUTION [1]*4/5
	self.key_A = FallingPiece(self.key_A_images, 60)
	self.key_A.location = (self.left_space+1*self.space,  self.key_position_y)
	self.key_A.image = self.key_A_images[2]
        self.key_A.destination = self.key_A.location

        self.key_B = FallingPiece(self.key_B_images, 60)
	self.key_B.location = (self.left_space+2*self.space,  self.key_position_y)
	self.key_B.image = self.key_B_images[2]
        self.key_B.destination = self.key_B.location

        self.key_C = FallingPiece(self.key_C_images, 60)
	self.key_C.location = (self.left_space+3*self.space, self.key_position_y)
	self.key_C.image = self.key_C_images[2]
        self.key_C.destination = self.key_C.location
                
        self.key_D = FallingPiece(self.key_D_images, 60)
	self.key_D.location = (self.left_space+4*self.space,  self.key_position_y)
	self.key_D.image = self.key_D_images[2]
        self.key_D.destination = self.key_D.location
                
        self.key_E = FallingPiece(self.key_E_images, 60)
	self.key_E.location = (self.left_space+5*self.space,  self.key_position_y)
	self.key_E.image = self.key_E_images[2]
        self.key_E.destination = self.key_E.location
        
                
	self.fire = FallingPiece(self.fire_images, 60)
	self.fire.location = Vector2(self.left_space+1*self.space,  self.key_position_y-25)
	self.fire.image = self.fire_images[0]
        self.fire.destination = Vector2(self.left_space+1*self.space,  self.key_position_y-45)
        
        self.light = FallingPiece(self.light_images, 60)
	self.light.location = Vector2(-40,-320)
	self.light.image = self.fire_images[0]
        self.lightright = FallingPiece(self.lightright_images, 60)
	self.lightright.location = Vector2(300,-290)
	self.lightright.image = self.fire_images[0]
        self.light.destination = self.light.location
        self.lightright.destination = self.lightright.location

        
	self.elements.append(self.key_A)
        self.elements.append(self.key_B)
        self.elements.append(self.key_C)
        self.elements.append(self.key_D)
        self.elements.append(self.key_E)
        self.elements.append(self.fire)
        self.elements.append(self.light)
        self.elements.append(self.lightright) 
      
                
	###############################################################
	###########  Falling piece reading              ###############
	###############################################################

        model=Score(self.song)
        model.readRythm()
        stuff=model.translateRythm()
        #print stuff
	length=len(stuff)
        self.totalnote=length
        self.countDown=length
	touch_line = self.key_position_y+100
        #print touch_line
        self.piece=[]
        #print stuff[0]
        for i in xrange(length):
            self.piece.append(FallingPiece(self.piece_A_images, 60))
            x,y,color=stuff[length-i-1]
            self.piece[i].location=Vector2(x,y)
	    self.piece[i].label=color
            self.piece[i].image=self.piece_A_images[5]
            self.piece[i].destination=Vector2(x,500)
#
            if color==1:
                #self.piece[i].speed=speed
		x,y=self.key_A.location 
                self.piece[i].destination = Vector2(x-20, touch_line)
	    elif color==2:
	       x,y=self.key_B.location 
	       self.piece[i].destination = Vector2(x-10, touch_line)
#	    elif color==3:
#	       #x,y=self.key_C.location 
#	       #self.piece[i].speed=speed
#	       #self.piece[i].destination = Vector2(x, touch_line)
	    elif color==4:
	       x,y=self.key_D.location 
	       self.piece[i].destination = Vector2(x+30, touch_line)
	    elif color==5:
	       x,y=self.key_E.location 
	       self.piece[i].destination = Vector2(x+50, touch_line)
	    self.elements.append(self.piece[i])


    def Effect(self):
        ####################################################
        #for 3D effect reset the x axil
        ####################################################
        spaceangle=50
        xc,ycenter= self.key_C.location
        xcenter=xc+20
        for i in xrange(len(self.piece)-1,0,-1):		    
             uselessx,y=self.piece[i].location
             
             if -10>y>-150:
                if self.piece[i].label==1:
                    self.piece[i].location=(xcenter-spaceangle*1,y)
                elif self.piece[i].label==2:
                    self.piece[i].location=(xcenter-spaceangle*0.7,y)
                elif self.piece[i].label==3:
                    self.piece[i].location=(xcenter-30,y)
                elif self.piece[i].label==4:
                    self.piece[i].location=(xcenter,y)
                elif self.piece[i].label==5:
                    self.piece[i].location=(xcenter,y)

             if 10>y>0:
                self.piece[i].image=self.piece_A_images[0]					
             elif 30>y>=10:
                self.piece[i].image=self.piece_A_images[1]
             elif 50>y>=30:
                self.piece[i].image=self.piece_A_images[2]
             elif 70>y>=50:
                self.piece[i].image=self.piece_A_images[3]
             elif 90>y>=70:
                self.piece[i].image=self.piece_A_images[4]
             elif 100>y>=90:
                self.piece[i].image=self.piece_A_images[5]
             elif y>=100:
                self.piece[i].image=self.piece_A_images[6]
             #if 402>y>400:
             #   #print "here"
             #   self.countDown-=1
        
             #self.endflag=1
        ##for i in xrange(len(self.piece)-1,0,-1):		    
        #    #y=self.piece[i].location
        #     if y<450:
        #        self.endflag=0
        #     if self.endflag!=0:
        #         print "end"
       # return self.flag_key
        #####################################################################   
        ########here when the piece enter key area. Turn the flag of key to 1
        ######################################################################    
             threhold=30
             if abs(y-self.key_position_y)<threhold:
                if self.piece[i].label==1:
                    self.flag_key[0]=1
                    self.flag_key[1]=0
                    self.flag_key[2]=0
                    self.flag_key[3]=0
                    self.flag_key[4]=0
                    
                    #print "bian1"
                elif self.piece[i].label==2:
                    self.flag_key[0]=0
                    self.flag_key[1]=1
                    self.flag_key[2]=0
                    self.flag_key[3]=0
                    self.flag_key[4]=0
                    #print "bian2"
                elif self.piece[i].label==3:
                    self.flag_key[0]=0
                    self.flag_key[1]=0
                    self.flag_key[2]=1
                    self.flag_key[3]=0
                    self.flag_key[4]=0
                    #print "bian3"
                    
                elif self.piece[i].label==4:
                    self.flag_key[0]=0
                    self.flag_key[1]=0
                    self.flag_key[2]=0
                    self.flag_key[3]=1
                    self.flag_key[4]=0
        
                    #print "bian4"
                elif self.piece[i].label==5:
                    self.flag_key[0]=0
                    self.flag_key[1]=0
                    self.flag_key[2]=0
                    self.flag_key[3]=0
                    self.flag_key[4]=1
         
                    #print "bian5"
        #print self.flag_key
        #self.endflag=1
        ##for i in xrange(len(self.piece)-1,0,-1):		    
        #    #y=self.piece[i].location
        #    if y<450:
        #        self.endflag=0
        #if self.endflag!=0:
        #    print "end"
        return self.flag_key
    
    def visionControlHandler(self,value):
        if value == [0,0,0,0,0]:
                        self.key_A.image = self.key_A_images[2]
                        self.key_B.image = self.key_B_images[2]
                        self.key_C.image = self.key_C_images[2]
                        self.key_D.image = self.key_D_images[2]
                        self.key_E.image = self.key_E_images[2]
    
        if value != [0,0,0]:
            if value[0] == 1:
                self.key_A.image = self.key_A_images[1]
                if  self.flag_key[0]==1:
                     pygame.mixer.music.set_volume(1.0)
                     self.key_A.image = self.key_A_images[0]
                     print "good"
                     self.scoreNum+=1
                else:
                     pygame.mixer.music.set_volume(0.3)
                     self.fail.play()
                     print "fail"
                #self.flag_key[0]=0
                
            elif value[1] == 2:
                self.key_B.image = self.key_B_images[1]
                if  self.flag_key[1]==1:
                     pygame.mixer.music.set_volume(1.0)
                     self.key_B.image = self.key_B_images[0]
                     print "good"
                     self.scoreNum+=1
                else:
                     pygame.mixer.music.set_volume(0.3)
                     self.fail.play()
                     print "fail"
                #self.flag_key[0]=0
                
            elif value[2] == 3:
                self.key_C.image = self.key_C_images[1]
                if  self.flag_key[2]==1:
                     pygame.mixer.music.set_volume(1.0)
                     self.key_C.image = self.key_C_images[0]
                     print "good"
                     self.scoreNum+=1
                else:
                     pygame.mixer.music.set_volume(0.3)
                     self.fail.play()
                     print "fail"
                #self.flag_key[0]=0
                
            elif value[3] == 4:
                self.key_D.image = self.key_D_images[1]
                if  self.flag_key[3]==1:
                     pygame.mixer.music.set_volume(1.0)
                     self.key_D.image = self.key_D_images[0]
                     print "good"
                     self.scoreNum+=1
                else:
                     pygame.mixer.music.set_volume(0.3)
                     self.fail.play()
                     print "fail"
                #self.flag_key[0]=0
                
            elif value[4] == 5:
                self.key_E.image = self.key_E_images[1]
                if  self.flag_key[4]==1:
                     pygame.mixer.music.set_volume(1.0)
                     self.key_E.image = self.key_E_images[0]
                     print "good"
                     self.scoreNum+=1
                else:
                     pygame.mixer.music.set_volume(0.3)
                     self.fail.play()
                     print "fail"
                #self.flag_key[0]=0
            
    
    
    def event_handler(self,event):
        if event.type == pygame.KEYUP:
                        self.key_A.image = self.key_A_images[2]
                        self.key_B.image = self.key_B_images[2]
                        self.key_C.image = self.key_C_images[2]
                        self.key_D.image = self.key_D_images[2]
                        self.key_E.image = self.key_E_images[2]
                        self.fire.image = self.fire_images[0]
                        self.light.image = self.light_images[0]
                        self.lightright.image = self.lightright_images[0]
                        

        if event.type == pygame.KEYDOWN:
                
                
                if event.key == K_1:
                        self.key_A.image = self.key_A_images[1]
                        if  self.flag_key[0]==1:
                             pygame.mixer.music.set_volume(1.0)
                             self.key_A.image = self.key_A_images[0]
                             self.fire.location = Vector2(self.left_space+1*self.space,  self.key_position_y-25)
                             self.fire.destination = Vector2(self.left_space+1*self.space,  self.key_position_y-45)
                             self.fire.image = self.fire_images[1]
                             self.lightright.image = self.lightright_images[1]
                             self.scoreNum+=1
                             print "good"
                        else:
                             pygame.mixer.music.set_volume(0.3)
                             self.fail.play()
                             #self.fire.image = self.fire_images[1]
                             print "fail"
                        #self.flag_key[0]=0
                elif event.key == K_2:
                        self.key_B.image = self.key_B_images[1]
                        if  self.flag_key[1]==1:
                             pygame.mixer.music.set_volume(1.0)
                             self.key_B.image = self.key_B_images[0]
                             self.fire.location = Vector2(self.left_space+2*self.space,  self.key_position_y-25)
                             self.fire.destination = Vector2(self.left_space+2*self.space,  self.key_position_y-45)
                             self.fire.image = self.fire_images[1]
                             self.light.image = self.light_images[1]
                             self.scoreNum+=1
                             print "good"
                        else:
                             pygame.mixer.music.set_volume(0.3)
                             self.fail.play()
                             print "fail"
                        #self.flag_key[1]=0
                        
                elif event.key == K_3:
                        self.key_C.image = self.key_C_images[1]
                        if  self.flag_key[2]==1:
                             pygame.mixer.music.set_volume(1.0)
                             self.key_C.image = self.key_C_images[0]
                             self.fire.location = Vector2(self.left_space+3*self.space,  self.key_position_y-25)
                             self.fire.destination = Vector2(self.left_space+3*self.space,  self.key_position_y-45)
                             self.fire.image = self.fire_images[1]
                             self.light.image = self.lightright_images[1]
                             self.light.image = self.light_images[1]
                             self.scoreNum+=1
                             print "good"
                        else:
                             pygame.mixer.music.set_volume(0.3)
                             self.fail.play()
                             print "fail"
                        #self.flag_key[2]=0
                elif event.key == K_4:
                        self.key_D.image = self.key_D_images[1]
                        if  self.flag_key[3]==1:
                             pygame.mixer.music.set_volume(1.0)
                             self.key_D.image = self.key_D_images[0]
                             self.fire.location = Vector2(self.left_space+4*self.space,  self.key_position_y-25)
                             self.fire.destination = Vector2(self.left_space+4*self.space,  self.key_position_y-45)
                             self.fire.image = self.fire_images[1]
                             #screen.blit(self.backb3, (0, 0))
                             self.lightright.image = self.lightright_images[1]
                             self.scoreNum+=1
                             print "good"
                        else:
                             pygame.mixer.music.set_volume(0.3)
                             self.fail.play()
                             print "fail"
                        #self.flag_key[3]=0
                elif event.key == K_5:
                        self.key_E.image = self.key_E_images[1]
                        if  self.flag_key[4]==1:
                             pygame.mixer.music.set_volume(1.0)
                             self.key_E.image = self.key_E_images[0]
                             self.fire.location = Vector2(self.left_space+5*self.space,  self.key_position_y-25)
                             self.fire.destination = Vector2(self.left_space+5*self.space,  self.key_position_y-45)
                             self.fire.image = self.fire_images[1]
                             self.light.image = self.light_images[1]
                             self.light.image = self.lightright_images[1]
                             self.scoreNum+=1
                             print "good"
                        else:
                             pygame.mixer.music.set_volume(0.3)
                             self.fail.play()
                             print "fail"
                #elif event.key == K_ESCAPE:
                        #print "here"
                        #exit()
        if event.type == QUIT:
                        return

################
####main code
###################
RESOLUTION = [800, 500]
pygame.init()
pygame.mixer.pre_init(44100,-16,2, 1024)
screen = pygame.display.set_mode((RESOLUTION[0],RESOLUTION [1]))
background = pygame.Surface(RESOLUTION)

class MainGame(object):
    def __init__(self,controlstate,song):
        #pygame.mixer.music.load(str(MUSIC_PATH)+"Send Him Away.ogg")                  #sound should be read based on songlist  
        pygame.mixer.music.load(str(MUSIC_PATH)+song+".ogg")
        default_font = pygame.font.get_default_font()
        font = pygame.font.SysFont(default_font, 20, False)	
        self.bb3=str(IMAGE_PATH)+"back_game7.png"
        self.b3=str(IMAGE_PATH)+"back_game4.png"
        self.back3=pygame.image.load(self.b3).convert_alpha()
        self.back3= pygame.transform.scale(self.back3, (RESOLUTION[0],RESOLUTION [1])).convert_alpha()
        self.backb3=pygame.image.load(self.bb3).convert_alpha()
        self.backb3= pygame.transform.scale(self.backb3, (RESOLUTION[0],RESOLUTION [1])).convert_alpha()
        self.font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
        background.fill((255,255,255))
        screen.blit(self.back3, (0, 0))
        if controlstate==0:
            self.aa=visionPart(0)
    
    
    def update(self,game,event):
        game.event_handler(event)
        
    def runMainGame(self,game,clock,controlstate):
        game.Effect()
        
        #for event in pygame.event.get():
                        #pygame.event.pump()
                        #game.event_handler(event)
        if controlstate==0: 
            mm=self.aa.visonInWhile()
            game.visionControlHandler(mm)
        screenWidth=600      
        flag_key=[0,0,0,0,0]
        #print game.scoreNum
       
        text = create_text("SCORE   ", self.font_preferences, 20, (228, 248, 254))
        textScore = create_text(str(game.scoreNum*85), self.font_preferences, 30, (218, 238, 234))
        #print game.countDown       
        game.accuracy=100.0*game.scoreNum/game.totalnote
        #textAcc = create_text("Accuracy   "+str(game.accuracy*100), self.font_preferences, 30, (0, 128, 0))
        time_passed = clock.tick(60)
        time_passed_seconds = time_passed / 1000.0
        
        screen.blit(self.back3, (0, 0))
        for game.element in game.elements:
                game.element.update(pygame.time.get_ticks())
                game.element.process(time_passed_seconds)
                game.element.render(screen)
        #pygame.transform.scale2x(game.light.image)
        #screen.blit(self.backb3, (0, 0))
        screen.blit(text,
        (70, 270+text.get_height() // 2))
        screen.blit(textScore,
        (50, 290+text.get_height() // 2))
        pygame.display.flip()
        return game.scoreNum*85,game.accuracy

#
#def run():        
#    pygame.key.set_repeat()
#    clock = pygame.time.Clock()
#    pause=False    
#    game=runPiece()
#    score=0
#    flag_key=[0,0,0,0,0]
#
#    controlstate=1
#    #hhh=MainGame(controlstate,"Send Him Away")
#    hhh=MainGame(controlstate,"hero")
#    state=9
#    #if state==9:
#    pygame.mixer.music.play()
#    while True:
#        #if state==9 :
#        for event in pygame.event.get():
#             #pass
#             hhh.update(game,event)
#        score=hhh.runMainGame(game,clock,controlstate)
#        print score            
#                    
#
#
#if __name__ == "__main__":
#				run()
