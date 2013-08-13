import pygame
import sys
from pygame.locals import *
class EzMenu:

    def __init__(self, *options):
        """Initialise the EzMenu! options should be a sequence of lists in the
        format of [option_name, option_function]"""

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()
        #load sound effect          
        self.in_sound = pygame.mixer.Sound("C:\Users\RUI YANG\Desktop/112finalroject/try\UI\SOUND\in.ogg")
        self.out_sound = pygame.mixer.Sound("C:\Users\RUI YANG\Desktop/112finalroject/try\UI\SOUND\out.ogg")
        self.crunch_sound = pygame.mixer.Sound("C:\Users\RUI YANG\Desktop/112finalroject/try\UI\SOUND\crunch.ogg")
    def play_in_sound(self):
        self.in_sound.play()
    def play_out_sound(self):
        self.out_sound.play()
    def play_crunch_sound(self):
        self.crunch_sound.play()

    def draw(self, surface):
        """Draw the menu to the surface."""
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1
            
    def update(self, event):
        """Update the menu and get input for the menu."""
        #for e in events:
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                self.option += 1
                self.play_crunch_sound()
                
            if event.key == K_UP:
                self.option -= 1
                self.play_crunch_sound()
            if event.key == K_RETURN:
                self.options[self.option][1]()
                self.play_in_sound()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1
            
            
   

    def set_pos(self, x, y):
        """Set the topleft of the menu at x,y"""
        self.x = x
        self.y = y
        
    def set_font(self, font):
        """Set the font used for the menu."""
        self.font = font
        
    def set_highlight_color(self, color):
        """Set the highlight color"""
        self.hcolor = color
        
    def set_normal_color(self, color):
        """Set the normal color"""
        self.color = color
        
    def center_at(self, x, y):
        """Center the center of the menu at x,y"""
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
