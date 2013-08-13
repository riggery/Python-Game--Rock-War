
import numpy as np
import sys
sys.path.append("/usr/local/lib/python2.7/site-packages/")
import cv
import cv2
import pygame
import pygame.midi
import pygame.mixer
from pygame.locals import *
from sys import exit
IMAGE_PATH = "C:\Users\RUI YANG\Desktop/112finalroject/try/UI/image/"
SOUND_PATH="C:\Users\RUI YANG\Desktop/112finalroject/try/UI/SOUND/"
MUSIC_PATH="C:\Users\RUI YANG\Desktop/112finalroject/try/UI/songs/"
pygame.init()
pygame.mixer.init


class detectHit(object):
	def __init__(self):
	        self.trace=[]
		self.tom01=pygame.mixer.Sound(str(SOUND_PATH)+'tom01.ogg')
		self.tom02=pygame.mixer.Sound(str(SOUND_PATH)+'tom02.ogg')
		self.tom03=pygame.mixer.Sound(str(SOUND_PATH)+'tom03.ogg')
		self.crash=pygame.mixer.Sound(str(SOUND_PATH)+'crash.ogg')
		#self.hitlabel=[0,0,0]
		self.hitlabel=0
	def detect(self,mx,my,left,right,top,bottom,drumlabel):
		if (left<mx<right and top<my<bottom):
		     #if self.trace!=[]:
			if drumlabel==1:
			      #self.tom01.play()
			      print "1played"
			      self.trace=[]
			      self.hitlabel=1
			      #self.hitlabel=[1,0,0]
			elif drumlabel==2:
			      #self.tom02.play()
			      self.trace=[]
			      print "2played"
			      self.hitlabel=2
			      #self.hitlabel=[0,2,0]
			elif drumlabel==3:
			     # self.tom03.play()
			      self.trace=[]
			      print "3played"
			      self.hitlabel=3
			elif drumlabel==4:
			      #self.tom02.play()
			      self.trace=[]
			      print "4played"
			      self.hitlabel=4
			      #self.hitlabel=[0,2,0]
			elif drumlabel==5:
			      #self.tom03.play()
			      self.trace=[]
			      print "5played"
			      self.hitlabel=5	
		#elif  (mx>right or mx<left or my<top or my>bottom) and self.trace==[]:
		elif  (mx>right or mx<left or my<top or my>bottom):
		      print "outside"
		      self.trace.append((mx,my))
		      self.hitlabel=0
		      #self.hitlabel=[0,0,0]
		return self.hitlabel

        def detectWithSound(self,mx,my,left,right,top,bottom,drumlabel):
		if (left<mx<right and top<my<bottom):
		     print self.trace
		     if self.trace!=[]:
			if drumlabel==1:
			      self.tom01.play()
			      print "1played"
			      self.trace=[]
			      self.hitlabel=1
			      #self.hitlabel=[1,0,0]
			elif drumlabel==2:
			      self.tom02.play()
			      self.trace=[]
			      print "2played"
			      self.hitlabel=2
			      #self.hitlabel=[0,2,0]
			elif drumlabel==3:
			      self.tom03.play()
			      self.trace=[]
			      print "3played"
			      self.hitlabel=3
			elif drumlabel==4:
			      self.tom02.play()
			      self.trace=[]
			      print "4played"
			      self.hitlabel=4
			      #self.hitlabel=[0,2,0]
			elif drumlabel==5:
			      self.crash.play()
			      self.trace=[]
			      print "5played"
			      self.hitlabel=5
			#elif drumlabel==6:
			#      #self.crash.play()
			#      cv.DestroyWindow("Real")
			#      self.trace=[]
			#      print "kill"
			#      self.hitlabel=6	
		elif  (mx>right or mx<left or my<top or my>bottom) and self.trace==[]:
		      print "outside"
		      self.trace.append((mx,my))
		      self.hitlabel=0
		      #self.hitlabel=[0,0,0]
		return self.hitlabel

			      
		      
class visionPart(detectHit):		      
	def __init__(self,state):
		self.state=state
		self.capture=cv.CaptureFromCAM(0)
		self.frame = cv.QueryFrame(self.capture)
		self.frame_size = cv.GetSize(self.frame)
		self.grey_image = cv.CreateImage(cv.GetSize(self.frame), cv.IPL_DEPTH_8U, 1)
		self.test=cv.CreateImage(cv.GetSize(self.frame),8,3)
		self.img2=cv.CreateImage(cv.GetSize(self.frame),8,3)
		cv.NamedWindow("Real",0)
		#cv.NamedWindow("Threshold",0)
		#cv.NamedWindow("Final",0)
		#cv.NamedWindow("Transparency",0)
		background_image_filename =str(IMAGE_PATH)+'drum.png'
		mouse_image_filename = str(IMAGE_PATH)+'guitarcursor.png'
		#self.background = pygame.image.load(background_image_filename).convert()
		#self.mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
		self.posx=0
		self.posy=0
		self.drumAHit=detectHit()        
	        self.drumBHit=detectHit()
	        self.drumCHit=detectHit()
		self.drumDHit=detectHit()        
	        self.drumEHit=detectHit()
		self.value=[0,0,0,0,0]
	
        		      
	def getthresholdedimg(self,im):
		'''this function take RGB image.Then convert it into HSV for easy colour detection and threshold it with yellow part as white and all other regions as black.Then return that image'''
		imghsv=cv.CreateImage(cv.GetSize(im),8,3)
		cv.CvtColor(im,imghsv,cv.CV_BGR2HSV)				# Convert image from RGB to HSV
		imgblue=cv.CreateImage(cv.GetSize(im),8,1)
		imgthreshold=cv.CreateImage(cv.GetSize(im),8,1)
		cv.InRangeS(imghsv,cv.Scalar(100,100,100),cv.Scalar(120,255,255),imgblue)	# Select a range of blue color
		cv.Add(imgthreshold,imgblue,imgthreshold)
		return imgthreshold

        def visonInWhile(self):
	       screenw=640
	       color_image = cv.QueryFrame(self.capture)
	       cv.Rectangle(color_image, (screenw-30,200),(screenw-110,300), cv.CV_RGB(0,153,0),2)
	       cv.Rectangle(color_image, (screenw-150,300),(screenw-230,400), cv.CV_RGB(153,0,0), 2)
	       cv.Rectangle(color_image, (screenw-270,350),(screenw-350,450), cv.CV_RGB(204,204,51), 2)
	       cv.Rectangle(color_image, (screenw-390,300),(screenw-470,400), cv.CV_RGB(0,102,0), 2)
	       cv.Rectangle(color_image, (screenw-510,200),(screenw-590,300), cv.CV_RGB(153,102,0), 2)
	       cv.Rectangle(color_image, (screenw-510,0),(screenw-590,10), cv.CV_RGB(153,202,202), 2)
	
	      
	       imdraw=cv.CreateImage(cv.GetSize(self.frame),8,3)
	       cv.SetZero(imdraw)
	       cv.Flip(color_image,color_image,1)
	       cv.Smooth(color_image, color_image, cv.CV_GAUSSIAN, 3, 0)
	       imgyellowthresh=self.getthresholdedimg(color_image)
	       cv.Erode(imgyellowthresh,imgyellowthresh,None,3)
	       cv.Dilate(imgyellowthresh,imgyellowthresh,None,10)
	       img2=cv.CloneImage(imgyellowthresh)
	       storage = cv.CreateMemStorage(0)
	       contour = cv.FindContours(imgyellowthresh, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
	       points = []
	       old_posx=0
	       old_posy=0
	       while contour:
		   bound_rect = cv.BoundingRect(list(contour))
		   contour = contour.h_next()
		   pt1 = (bound_rect[0], bound_rect[1])
		   pt2 = (bound_rect[0] + bound_rect[2], bound_rect[1] + bound_rect[3])
		   points.append(pt1)
		   points.append(pt2)
		   cv.Rectangle(color_image, pt1, pt2, cv.CV_RGB(255,0,0), 2)
		   posx=cv.Round((pt1[0]+pt2[0])/2)
		   posy=cv.Round((pt1[1]+pt2[1])/2)    
		   if abs(posx-old_posx)>30 or abs(posy-old_posy)>30:
		       x,y=posx,posy
		       old_posx=posx
		       old_posy=posy
		   else:
		       x,y=old_posx,old_posy
		       old_posx=posx
		       old_posy=posy
		   #x,y=posx,posy
		   #print x,y
		   self.value=[0,0,0,0,0]
		   if self.state==0:
			self.value[0]=self.drumAHit.detect(x,y,30,110,200,300,1)
			self.value[1]=self.drumBHit.detect(x,y,150,230,300,400,2)
			self.value[2]=self.drumCHit.detect(x,y,270,350,350,450,3)
			self.value[3]=self.drumDHit.detect(x,y,390,470,300,400,4)
			self.value[4]=self.drumEHit.detect(x,y,510,590,200,300,5)
		   
		   elif self.state==1:
			self.value[0]=self.drumAHit.detectWithSound(x,y,30,110,200,300,1)
			self.value[1]=self.drumBHit.detectWithSound(x,y,150,230,300,400,2)
			self.value[2]=self.drumCHit.detectWithSound(x,y,270,350,350,450,3)
			self.value[3]=self.drumDHit.detectWithSound(x,y,390,470,300,400,4)
			self.value[4]=self.drumEHit.detectWithSound(x,y,510,590,200,300,5)
			#self.value[4]=self.drumEHit.detectWithSound(x,y,510,590,0,10,6)
	       
	       font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 0, 1)
	       cv.Add(self.test,imdraw,self.test)
	       cv.ShowImage("Real",color_image)
	       #return self.value
	       if cv.WaitKey(33)==1048603:
		       cv.DestroyWindow("Real")
		       #cv.DestroyWindow("Threshold")
		       #cv.DestroyWindow("Final")
	       return self.value
	
	       
#
#aa=visionPart(1)
#while True:
#    label=aa.visonInWhile()
#    print 
#    #print label