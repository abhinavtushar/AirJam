#Module to play sound
import subprocess
import thread

def play_guitar(notes, delay, fade):
	notes_array = notes.split(" ")
	final_string = ""
	for i in notes_array:
		final_string += "pl " + i + " "
	if delay != 0:
		two_places = decimal.Decimal('10')**-2
		i = 0
		final_string += "delay "
		while i < len(notes_array):
			final_string += str(decimal.Decimal(delay * i).quantize(two_places)) + " "
			i += 1
	i = 0
	if fade != [0, 0, 0]:
		final_string += "remix - fade "
		while i < len(fade):
			final += str(fade[i]) + " "
			i += 1
		final_string += "norm -1"
	subprocess.call("play -n synth " + final_string, shell = True)

def play_drum(type):
	# Plays the drum according to the type
	return

def play(instrument, params):
	if instrument == 'guitar':
		thread.start_new_thread(play_guitar, (params[0], 0.05, [0, 4, 0.1]))
	if instrument == 'drums':
		thread.start_new_thread(play_drum, (params[0]))