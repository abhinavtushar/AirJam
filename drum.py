import cv2
import numpy as np
import lib

vc = cv2.VideoCapture(0)

# Initialize
ret, frame = vc.read()

HEIGHT = frame.shape[0]
WIDTH = frame.shape[1]
DRUMS_ARRAY = lib.create_drums(HEIGHT, WIDTH)

def draw(img):
	# Draws the drum circles on the frames
	return img_with_drums

while ret:
	hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	# Filter red drumstick head and get position
	position = # To get
	cv2.imshow('Preview', draw(frame))

	for drum in DRUMS_ARRAY:
		drum.check(position)
	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break