# The Air guitar

import lib.imgproc as imgproc
import lib.guitarproc as guitarproc
import cv2
import time

#----------------------------------------------------------

vc = cv2.VideoCapture(0)

#Initialize and configure
time.sleep(3)

ret, frame = vc.read()

if ret:

	# Cropping the ROI
	height = frame.shape[0]
	width = frame.shape[1]
	finger_frame = frame[0:(height/2), (width/2):(width-1)]
	lower_frame = frame[(height/2):(height-1), 0:(width/2)]

	finger_images = []
	for color in ["red", "green", "blue"]:
		finger_images.append(imgproc.filter_color(finger_frame, color))
	finger_positions = []
	for finger_img in finger_images:
		finger_positions.append(imgproc.get_position(finger_img))

	lower_position = imgproc.get_position(imgproc.filter_color(lower_frame, "red"))
	guitarproc.init_neck(finger_positions[0],lower_position)

#----------------------------------------------------------

ret, frame = vc.read()

# Motion detection flags
prev_position = 0
direction = 0
up = 0
down = 0
first_frame = 1

while ret:

	# Cropping the ROI
	height = frame.shape[0]
	width = frame.shape[1]
	finger_frame = frame[0:(height/2), (width/2):(width-1)]
	lower_frame = frame[(height/2):(height-1), 0:(width/2)]

	finger_images = []
	for color in ["red", "green", "blue"]:
		finger_images.append(imgproc.filter_color(finger_frame, color))

	finger_positions = []
	for finger_img in finger_images:
		finger_positions.append(imgproc.get_position(finger_img))

	# Detect the mode of playback
	mode = guitarproc.get_mode(finger_positions)
	distance = guitarproc.get_distance(finger_positions)

	# Show the mode on screen
	cv2.putText(frame, mode , (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, 255)
	cv2.imshow('Preview', frame)
		
	# Find the postion of lower strumming hand
	lower_position = imgproc.get_position(imgproc.filter_color(lower_frame, "red"))

	# Motion detection for lower hand
	if prev_position != 0:
		disp = lower_position[0][1] - prev_position
		direction = direction + disp
		if direction < -200:
			up = 1
			direction = 0
		if direction > 200:
			down = 1
			direction = 0
	if first_frame == 1:
		first_frame = 0
	prev_position = lower_position[0][1]
		
	# Perform the playback
	if down == 1:
		guitarproc.strum(mode,distance,'down')
		down = 0

	else:
		if up == 1:
			guitarproc.strum(mode,distance,'up')
			up = 0

	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break

cv2.destroyAllWindows()

#----------------------------------------------------------