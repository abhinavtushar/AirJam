# Routines related to guitar

import playback

#----------------------------------------------------------

neck_len=500
neck_top=0
neck_bottom=500

# Notes making each chords in Standard Guitar Tuning

strums = {
	'A': [(3,7),(2,4),(3,0),(2,7),(1,0),(1,7)],
	'C': [(3,7),(2,3),(10,2),(2,7),(1,3),(1,7)],
	'D': [(3,9),(2,5),(3,0),(2,5),(1,0),(1,7)],
	'E': [(3,7),(2,2),(2,11),(2,7),(1,2),(1,7)],
	'G': [(3,10),(2,2),(2,10),(2,5),(1,2),(1,10)]}

# Array to go over each note in case of fret shift

notes_ar = [['A1','A#1','B1','C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1'],
		['A2','A#2','B2','C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2'],
		['A3','A#3','B3','C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3'],
		['A4','A#4','B4','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4'],
		['A5','A#5','B5','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5']]

#----------------------------------------------------------

def get_mode(position_array):
	# Get the mode of playback
	R=position_array[0][1]
	G=position_array[1][1]
	B=position_array[2][1]

	if R<G<B:
		mode='A'

	elif B<G<R:
		mode='C'

	elif R<B<G: 
		mode='D'

	elif G<B<R:
		mode='E'

	else:
		mode='G'

	return mode

#----------------------------------------------------------

def strum(mode, dist, direction):
	# Play the given mode
	pattern=''
	for note in strums[mode]:
		if note[1]+dist>11:
			pattern=pattern+notes_ar[note[0]+1][(note[1]+dist)%12]+' '
		else:
			try:
				pattern=pattern+notes_ar[note[0]][(note[1]+dist)%12]+' '
			except IndexError:
				return

	if direction=='up':
		playback.play('guitar', pattern)
	else:
		rev = ""
		_array = pattern.split(" ")
		for row2 in reversed(_array):
			rev += row2 + " "
		playback.play('guitar', rev[:-1])

#----------------------------------------------------------

def init_neck(top, bottom):
	# Initialize the neck length
	neck_len=(top[0]-bottom[0][0])/2
	neck_bottom=bottom[0][0]
	neck_top=top[0]

#----------------------------------------------------------

def get_distance(positions):
	# Get Distance on the neck
	mean=0

	for pos in positions:
		mean+=pos[0]

	mean=neck_top-mean/3

	if mean > 3*neck_len/4:
		return 3
	elif mean > 2*neck_len/4:
		return 2
	elif mean > neck_len/4:
		return 1
	else:
		return 0

#----------------------------------------------------------