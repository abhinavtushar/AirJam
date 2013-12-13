# Routines related to drums

import math
import playback
import json

#----------------------------------------------------------

class drum:
	def __init__(self, x, y, radius, typ):
		self.position = (x, y)
		self.radius = radius
		self.type = typ
		self.stick_here = False
		self.play_flag = True

	def check(self, position):
		# Checks if the stick is on the drum
		distance = math.sqrt(((position[0]-self.x)**2)+((position[1]-self.y)**2))
		if distance <= self.radius and self.stick_here == False:
			self.stick_here = True

	def bang:
		# Plays the drum
		playback.play('drums', self.type)

#----------------------------------------------------------

def create_drums(frame):
	# Instantiates drums according to config ../config/drums.json and returns an array of drums
	height = frame.shape[0]
	width = frame.shape[1]
	# Read Config
	return drums_array

#----------------------------------------------------------

def draw_drums(img, DRUMS_ARRAY):
	# Draws drum circles on the frames
	for drum in DRUMS_ARRAY:
		img = cv2.circle(img, drum.position, drum.radius, (0, 255, 0), 2)
	return img

#----------------------------------------------------------