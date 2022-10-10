'''
Jerry Zheng
jz565@njit.edu
CS341 Section 007
'''

print("Project 1 for CS341\nSection number: 007\nSemester: Fall 2022\nWritten by: Jerry Zheng, jz565\n" + 
	"Instructor: Marvin Nakayama, marvin@njit.edu")

alpha = "1234567890"
r = "abcdefghijklmnopqrstuvwxyz"
rWithoutC = "abdefghijklmnopqrstuvwxyz"
rWithoutO = "abcdefghijklmnpqrstuvwxyz"
rWithoutM = "abcdefghijklnopqrstuvwxyz"

#Ask user if they want to enter 
userInput = input("Do you want to input a string? (y/n) ")
while userInput == 'y':
	print("y")
	s = input("Enter your string: ")
	print(s)
	
	#Starts in starting state q1
	state = "q1"
	print("State", state)

	#Loops through every character in the string from user input
	for char in s:	
		#Transitions from state q1
		if state == "q1":
			if char in r:
				state = "q3"
			else:
				state = "q2"

		#Transitions from state q2 (Trap State)
		elif state == "q2":
			state = "q2"

		#Transitions from state q3
		elif state == "q3":
			if char == "@":
				state = "q5"
			elif char == ".":
				state = "q4"
			elif char in alpha or char in r:
				state = "q3"

		#Transitions from state q4
		elif state == "q4":
			if char in r:
				state = "q3"
			elif char == ".":
				state = "q2"
			elif char == "@":
				state = "q2"
			elif char in alpha:
				state = "q2"

		#Transitions from state q5
		elif state == "q5":
			if char in r:
				state = "q6"
			else:
				state = "q2"

		#Transition from state q6
		elif state == "q6":
			if char in r or char in alpha:
				state = "q6"
			elif char == ".":
				state = "q7"
			elif char == "@":
				state = "q2"

		#Transition from state q7
		elif state == "q7":
			if char == "c":
				state = "q8"
			elif char == ".":
				state = "q2"
			elif char == "@":
				state = "q2"
			elif char in rWithoutC:
				state = "q6"
			elif char in alpha:
				state = "q2"

		#Transition from state q8
		elif state == "q8":
			if char == "o":
				state = "q9"
			elif char == ".":
				state = "q7"
			elif char == "@":
				state = "q2"
			elif char == alpha or char == rWithoutO:
				state = "q6"

		#Transition from state q9
		elif state == "q9":
			if char == "m":
				state = "q10"
			elif char == ".":
				state = "q7"
			elif char == "@":
				state = "q2"
			elif char == alpha or char == rWithoutM:
				state = "q6"

		#Transition from state q10
		elif state == "q10":
			if char in alpha or char in r:
				state = "q6"
			elif char == ".":
				state = "q7"
			elif char == "@":
				state = "q2"

		#Prints the final output
		print("Character", char)
		print("State", state)

	if (state == "q10"):
		print("String is accepted")
	else:
		print("String is rejected")

	userInput = input("Do you want to input a string? (y/n) ")

print("n")

