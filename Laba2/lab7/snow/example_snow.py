import pygame
import random
import example_snow_classes as classes

#цвета
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0 , 255)

#экрана параметры
pygame.init()

SIZE = (1200, 600)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('My snow')

clock = pygame.time.Clock()

#Звёзд массив
number_of_stars = 600
star_list = []

for i in range(number_of_stars):
	new_star = classes.rand_star(*SIZE)
	star_list.append(new_star)

#Условие завершения работы
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(black)

	for i in range(len(star_list)):
		pygame.draw.circle(screen, star_list[i].color , star_list[i].position, star_list[i].radius)
		star_list[i].new_position()
		if star_list[i].position[1] >= SIZE[1]:
			new_star = classes.rand_star(*SIZE, new = True)
			star_list[i] = new_star

	pygame.display.update()
	clock.tick(120)

pygame.quit()
