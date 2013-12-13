# Basic CV Routines

import cv2
import numpy as np
import math
import json

#----------------------------------------------------------

# Get range from ../config/color.json

#----------------------------------------------------------

def clear_noise(img):
	#Clears noise from image
	kernel = np.ones((10, 10), np.uint8)
	clrimg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
	clrimg = cv2.erode(img, kernel, iterations=1)
	kernel = np.ones((15, 15), np.uint8)
	clrimg = cv2.dilate(img, kernel, iterations=2)
	return clrimg

#----------------------------------------------------------

def filter_color(img, color):
	# Filter the color blob
	hsvframe = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	min_val = np.array("""min_h[color], min_s[color], min_v[color]""", np.uint8)
	max_val = np.array("""max_h[color], max_s[color], max_v[color]""", np.uint8)
	filtered = cv2.inRange(hsvframe, min_val, max_val)
	cleared = clear_noise(filtered)
	return cleared

#----------------------------------------------------------

def get_position(img):
	# Returns the largest blob's topmost point
	contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if len(contours)<1:
		return (0, 0)

	return tuple(contours[0][contours[0][:,:,1].argmin()][0])

#----------------------------------------------------------