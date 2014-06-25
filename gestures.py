#Draw gestures
#If a matching gesture is recognized, launch a program
#Ex, W gesture to launch Word
	#T gesture to launch terminal
	#Square to launch google maps

#Add "Deadzone" to prevent random jumping
#Check Relative Positions to determine direction
import pygame
import sys
import math
import re

patterns = ["1.*3.*5.*7","2.*8.*2.*8"]
process =  ["Square!", "W!", "V"]
last = " "
def compass (coords):
	#use tangent to find angle
	hyp = coords[0]**2 + coords[1]**2
	hyp = hyp**0.5
	if hyp != 0:
		ratio = -coords[1]/hyp
		angle = math.asin(ratio)
		angle = math.degrees(angle)
		global last
		if coords[0] < 0:
			angle *= -1
			angle += 180
		if angle < 22.5 and angle > -22.5 and last != "1":
			print "RIGHT"
			last = "1"
		elif angle < -22.5 and angle > -67.5 and last != "2":
			print "RIGHT-DOWN"
			last = "2"
		elif angle < -67.5 and angle > -90.1 and last != "3" or angle>247.5 :
			print "DOWN"
			last = "3"
		elif angle < 247.5 and angle > 202.5 and last != "4":
			print "DOWN-LEFT"
			last = "4"
		elif angle < 202.5 and angle > 157.5 and last != "5":
			print "LEFT"
			last = "5"
		elif angle < 157.5 and angle > 112.5 and last != "6":
			print "LEFT-UP"
			last = "6"
		elif angle < 112.5 and angle > 67.5 and last != "7":
			print "UP"
			last = "7"
		elif angle < 67.5 and angle > 22.5 and last != "8":
			print "UP-RIGHT"
			last = "8"
		else:
			return ""
		return last
	else:
		return ""


def findMatch (sequence): #Need to ignore some stuff/congestion
	#Use a regex to find a match
	global patterns
	for pattern in patterns:
		if re.search(pattern, sequence) != None:
			print "FOUND!"
			execute(patterns.index(pattern)) #Execute the proper function
			#need redundancy if it matches more than 1. Take the longer of the sequences

def execute (i):
	global process
	print "Executed process '" + process[i] + "'"

pygame.init()
window = pygame.display.set_mode((500,500)) #Creates 500x500 window


#Load Existing Gestures
#with f as open:
#Main Loop
while True:
	pattern = ""
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #Exit signal
			sys.exit(0)
		elif event.type == pygame.MOUSEBUTTONDOWN: #Button Press Detected
			held = True
			while held:
				pygame.time.wait(50)
				for event2 in pygame.event.get():
					if event2.type == pygame.MOUSEBUTTONUP:
						held = False
						print "Lifted"
					else:
						#Allocate relative to compass coords
						pattern += compass(pygame.mouse.get_rel())
			#Holding finished, should have an array of directions
			#Compare new array to loaded arrays from file
			#If match found, launch associated program with os.spawn or subprocess
			print pattern
			findMatch(pattern)