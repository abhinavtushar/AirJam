#Module to play sound
import subprocess
import thread

def _gen_string(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	notes_array = notes.split(" ")
	final = ""
	for i in notes_array:
		final += "pl " + i + " "
	if not delay_period == 0:
		two_places = decimal.Decimal ('10') ** -2
		j = 0
		final += "delay "
		while j < len(notes_array):			
			final += str(decimal.Decimal(delay_period * j).quantize(two_places)) + " "
			j += 1	

	j = 0
	if not fade == [0, 0, 0]:
		final += "remix - fade "
		while j < len(fade):
			final += str(fade[j]) + " "
			j += 1
		final += "norm -1"

	return final

def _play(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	subprocess.call("play -n synth " + _gen_string(notes, delay_period, fade), shell = True)
	return

def play(notes, delay_period = 0.05, fade = [0, 4, 0.1]):
	thread.start_new_thread(_play, (notes, delay_period, fade))