# The Air drum

import lib.drumproc as drumproc
import lib.imgproc as imgproc
import cv2

#----------------------------------------------------------

vc = cv2.VideoCapture(0)

#----------------------------------------------------------
# Initialize
ret, frame = vc.read()
DRUMS_ARRAY = drumproc.create_drums(frame)

#----------------------------------------------------------

while ret:
	# Filter red drumstick head and get position
	img = imgproc.filter_color(frame, "red")
	position = imgproc.get_position(img)

	frame = drumproc.draw_drums(frame, DRUMS_ARRAY)
	cv2.imshow('Preview', frame)

	for drum in DRUMS_ARRAY:
		if position != (0, 0):
			drum.check(position)
			if drum.stick_here == True and drum.play_flag == True:
				drum.bang()
				drum.play_flag = False
			else:
				drum.play_flag = True

	ret, frame = vc.read()
	key = cv2.waitKey(20)
	if key == 27:
		break

cv2.destroyAllWindows()

#----------------------------------------------------------