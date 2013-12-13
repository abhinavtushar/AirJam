# Routines related to drums

import math
import playback
import sys
sys.path.append("../config/")
import drums_config

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
	# Instantiates drums according to ../config/drums_config and returns an array of drums
	height = frame.shape[0]
	width = frame.shape[1]
	drums_array = []
	for i in range(NUMBER_OF_DRUMS):
		x = DRUM_SET[i]["cx"]*width
		y = DRUM_SET[i]["cy"]*height
		r = DRUM_SET[i]["r"]*width
		typ = DRUM_SET[i]["type"]
		drums_array.append(drum(x, y, r, typ))
	return drums_array

#----------------------------------------------------------

def draw_drums(img, DRUMS_ARRAY):
	# Draws drum circles on the frames
	for drum in DRUMS_ARRAY:
		img = cv2.circle(img, drum.position, drum.radius, (0, 255, 0), 2)
	return img

#----------------------------------------------------------