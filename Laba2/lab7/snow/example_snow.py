import pygame
import random
import example_snow_classes as classes
from math import *

#цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0 , 255)
yellow = (255,255,0)

#экрана параметры
pygame.init()
Screen_SIZE = [1200, 600]
STFALLSIZE = [Screen_SIZE[0],int(Screen_SIZE[1]/3)]

screen = pygame.display.set_mode(Screen_SIZE)
pygame.display.set_caption('My snow')

clock = pygame.time.Clock()

#Звёзд массив
number_of_stars = 600
#за солнце константы
sun_angle = 0
left_angle = 135
right_angle = 45
curr_angle = left_angle
angle_inc = -0.2
centr = [int(Screen_SIZE[0]*1/2), int(Screen_SIZE[1]*4/9)]

#Cloud
speed_x = 3
posx = 200

#man
man_c = white
leg_angle = 30
leg_angle_speed = 1
man2_x, man2_y = 1100, 220
man2_speed = 1 

star_list0 = classes.star_list(STFALLSIZE, number_of_stars)

def line(x, y, length, angle = 0,  color = white):
        rangle = radians(angle)
        x1 = x + cos(rangle)*length
        y1 = y - sin(rangle)*length
        pygame.draw.line(screen, color, [x,y], [x1,y1], 5)

def star_fall(x,y,SIZE, star_list):
        for i in range(len(star_list)):
                coord = [star_list[i].position[0]+x, star_list[i].position[1]+y]
                pygame.draw.circle(screen, star_list[i].color , coord, star_list[i].radius)
                star_list[i].new_position()
                if star_list[i].position[1]+y >= SIZE[1]+y :
                        new_star = classes.rand_star(*SIZE, new = True)
                        star_list[i] = new_star

def sun(x,y,radius, st_angle = 0):
        pygame.draw.circle(screen,yellow, [x,y], radius)
        for i in range(st_angle,st_angle + 360,18):
                line(x,y, radius*2, angle = i, color = yellow)

def cloud(x,y,radius):
        pygame.draw.circle(screen, white, [int(x-radius), int(y - radius*0.3)], radius)
        pygame.draw.circle(screen, white, [int(x), int(y - radius*0.3)], radius)
        pygame.draw.circle(screen, white, [int(x+radius), int(y - radius*0.3)], radius)
        pygame.draw.circle(screen, white, [int(x-radius*0.5), int(y+ radius*0.3)], radius)
        pygame.draw.circle(screen, white, [int(x+radius*0.5), int(y+ radius*0.3)], radius)
        

def mov_sun(x, y, curr_angle, orb_radius = 300):
        curr_rangle = radians(curr_angle)
        x = round(x + cos(curr_rangle)*orb_radius*2)
        y = round(y - sin(curr_rangle)*orb_radius)
        return x,y

def face(x,y, Rad = 15, angle = 90):
	rangle = radians(angle)
	x1,y1 = int(x + cos(rangle + radians(45))*Rad * 0.3), int(y - sin(rangle + radians(45))*Rad * 0.3)
	x2,y2 = int(x + cos(rangle - radians(45))*Rad * 0.3), int(y - sin(rangle - radians(45))*Rad * 0.3)
	pygame.draw.circle(screen, man_c, [x1,y1], int(Rad*0.3))
	pygame.draw.circle(screen, man_c, [x2,y2], int(Rad*0.3))
	x3,y3 = int(x + cos(rangle + radians(180))*Rad * 0.35), int(y - sin(rangle + radians(180))*Rad * 0.35) 
	line(x3,y3, Rad * 0.3, angle = angle - 90, color = man_c)
	line(x3,y3, Rad * 0.3, angle = angle + 90, color = man_c)

def man2(x,y, SIZE = 150):
	global leg_angle, leg_angle_speed
	line(x,y, SIZE/2, angle = 90, color = man_c)
	x1,y1 = x, int(y - SIZE * 0.65)
	pygame.draw.circle(screen, man_c, [x1, y1], int(SIZE*0.15),1)
	face(x1, y1, SIZE*0.15)
	line(x, y, SIZE*0.4, angle = -90 + leg_angle, color = man_c)
	line(x, y, SIZE*0.4, angle = -90 - leg_angle, color = man_c)
	leg_angle -= leg_angle_speed
	if (leg_angle >= 30) or (leg_angle <= -30):
		leg_angle_speed *=-1
        

#Условие завершения работы
done = False
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        done = True
        screen.fill(black)
        pygame.draw.rect(screen, (0,128,0), [0,int(Screen_SIZE[1]*3/9),
                                         Screen_SIZE[0],Screen_SIZE[1]])
        
        #star_fall(0, 0, STFALLSIZE, star_list0.list)
        
        
        #sun
        x,y  = mov_sun(centr[0],centr[1],curr_angle, orb_radius = int(Screen_SIZE[1]/3))
        sun(x,y,35, st_angle = sun_angle)
        sun_angle +=2
        curr_angle += angle_inc
        if (left_angle < curr_angle) or (curr_angle < right_angle):
                angle_inc *= -1
                
        #cloud
        cloud(posx,100,30)
        posx += speed_x
        if (posx <= 200) or (posx >= 1000):
                speed_x *= -1
        #road
        pygame.draw.polygon(screen, (255,128,0), [[0,500], 
        	[1200,210], [1200,260], [650,600], [0,600]])
        
        man2(man2_x,man2_y)
        if man2_x > 400:
        	man2_x -= 3
        if man2_y < 500:
        	man2_y += 1.5
        if (man2_x <= 400) and (man2_y >= 500):
        	leg_angle = 30
        	leg_angle_speed = 0
        pygame.display.update()
        clock.tick(60)
pygame.quit()
