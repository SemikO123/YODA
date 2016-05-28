import random

def random_RGB():
	R = random.randrange(0, 256)
	G = random.randrange(0, 256)
	B = random.randrange(0, 256)
	return (R, G, B)

# *-* Звёздочки *-*	
class rand_star:
	def __init__(self, width, height, new = False):
		x = random.randrange(0,width)
		if new:
			y = random.randrange(-40,10)
		else:
			y = random.randrange(0,height)
		
		radius = random.randrange(2,8)
		color = random_RGB() 
		speed_y = random.randrange(2,7)
		speed_x = random.randrange(-1,2)
		self.position = [x,y]
		self.radius = radius
		self.color = color
		self.speed_y = speed_y
		self.speed_x = speed_x

	def new_position(self):
		#self.position[0] += self.speed_x
		self.position[1] += self.speed_y
		
	def __str__(self):
		return '[%d,%d] radius=%d color=(%d,%d,%d)'  %( *self.position, self.radius, *self.color)

