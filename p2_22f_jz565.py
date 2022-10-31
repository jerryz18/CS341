'''
Jerry Zheng
jz565@njit.edu
CS341 Section 007
'''

print("Project 2 for CS341\nSection number: 007\nSemester: Fall 2022\nWritten by: Jerry Zheng, jz565\n" + 
	"Instructor: Marvin Nakayama, marvin@njit.edu")

digits = "1234567890"
operations = "+-/*"
print("NOTE: Operations (+-/*) will be represented by - in the stack")
userInput = input("Do you want to input a string? (y/n) ")

while userInput == 'y':
	stack = []
	crash = False
	print("y")
	s = input("Enter your string: ")
	print("Inputted String: ", s)
	
	#Starts in starting state q0
	state = "q0"

	#Loops through every character in the string from user input
	for char in s:
		print("Character read:", char)
		print("Current State:", state)
		print("Current Stack:", stack)

		#Transitions from state q0
		if state == "q0":
			if char == "%":
				state = "q1"
				stack.append(char)
				print("% was pushed onto the stack")
			else:
				crash = True
				break

		#Transitions from state q1
		elif state == "q1":
			if char == "(":
				state = "q1"
				stack.append(char)
				print("( was pushed onto the stack")
			elif char in digits:
				state = "q2"
			elif char == ".":
				state = "q3"
			else:
				crash = True
				break

		#Transitions from state q2
		elif state == "q2":
			if char in digits:
				state = "q2"
			elif char == ".":
				state = "q4"
			else:
				crash = True
				break

		#Transitions from state q3
		elif state == "q3":
			if char in digits:
				state = "q4"
			else:
				crash = True
				break

		#Transitions from state q4
		elif state == "q4":
			if char in digits:
				state = "q4"
			elif char == ")":
				pop = stack.pop()
				if pop != "(":
					print("Cannot pop ( from the stack")
					crash = True
					break
				else:
					print("( was popped from the stack")
			elif char in operations:
				state = "q5"
				stack.append("-")
				print(char, "was pushed onto the stack")
			elif char == "%":
				state = "q9"
				pop = stack.pop()
				if pop != "%":
					print("Cannot pop \'%\' from the stack")
					crash = True
					break
				else:
					print("% was popped from the stack")
			else:
				crash = True
				break

		#Transitions from state q5
		elif state == "q5":
			if char == "(":
				state = "q5"
				stack.append(char)
				print("( was pushed onto the stack")
			elif char in digits:
				state = "q6"
			elif char == ".":
				state = "q7"
				pop = stack.pop(stack.index("-"))
				if pop != "-":
					print("Cannot pop (+,-,/,*) from the stack")
					crash = True
					break
				else:
					print("(+,-,/,*) was popped from the stack")
			else:
				crash = True
				break

		#Transitions from state q6
		elif state == "q6":
			if char in digits:
				state = "q6"
			elif char == ".":
				state = "q8"
				pop = stack.pop(stack.index("-"))
				if pop != "-":
					print("Cannot pop (+,-,/,*) from the stack")
					crash = True
					break
				else:
					print("(+,-,/,*) was popped from the stack")
			else:
				crash = True
				break

		#Transitions from state q7
		elif state == "q7":
			if char in digits:
				state = "q8"
			else:
				crash = True
				break

		#Transitions from state q8
		elif state == "q8":
			if char in operations:
				state = "q5"
				stack.append("-")
				print(char, "was pushed onto the stack")
			elif char in digits:
				state = "q8"
			elif char == ")":
				state = "q8"
				pop = stack.pop()
				if pop != "(":
					print("Cannot pop ( from the stack")
					crash = True
					break
				else:
					print("( was popped from the stack")
			elif char == "%":
				state = "q9"
				pop = stack.pop()
				if pop != "%":
					print("Cannot pop \'%\' from the stack")
					crash = True
					break
				else:
					print("% was popped from the stack")
			else:
				crash = True
				break
		print("State after transition:", state)
		print()

	if crash == True:
		print("Final Stack:", stack)
		print("PDA has crashed before the competition of reading the string")
		print("String is rejected")
	elif state == "q9":
		print("Character read:", char)
		print("Current State:", state)
		print("Final Stack:", stack)
		print("String is accepted")

	userInput = input("Do you want to input a string? (y/n) ")

print("n")

