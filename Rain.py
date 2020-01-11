# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:55:29 2019

@author: shyan
"""

import pygame
import random

pygame.init()

x=1000
y=500
bg=(220,220,255)
colour=(0,0,90)

screen=pygame.display.set_mode((x,y))

class rain:
    def __init__(self):
        self.x1=random.randint(1,1000)
        self.y1=random.randint(-4000,-2000)
        self.ys=random.randint(14,17)
    def draw(self):
        self.y1+=self.ys
        if self.y1>500:
            self.x1=random.randint(1,1000)
            self.y1=random.randint(-800,-700)
            self.ys=random.randint(15,25)
        pygame.draw.rect(screen,(colour),(self.x1,self.y1,1,15))
    def call(self):
        self.draw()

a=[]
for i in range(500):
    a.append(rain())


while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(bg)
    for i in range(500):
        a[i].call()
    pygame.display.update()