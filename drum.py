import cv2
import lib

vc = cv2.VideoCapture(0)

# Initialize
ret, frame = vc.read()

DRUMS_ARRAY = lib.create_drums("drums_config.json", frame)

def draw(img, DRUMS_ARRAY):
	for drum in DRUMS_ARRAY:
		img = cv2.circle(img, drum.position, drum.radius, (0, 255, 0), 2)
	return img

while ret:
	# Filter red drumstick head and get position
	position = lib.find_position(frame, "red")

	cv2.imshow('Preview', draw(frame))

	for drum in DRUMS_ARRAY:
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