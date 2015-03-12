import turtle
import time
PEN_ON = "PEN_ON"
PEN_OFF = "PEN_OFF"
DOT = "DOT"


scale = lambda x : -x * 10
posistion = lambda x : 0 + scale(-3) * x
locationScale = lambda x,y : x + y
letters = {
	'NEXT':["NEXT"],
	##Steps
	#Implicit on
	#Starting point is the first instruction
	#Pen off implicit 
	'1': [[1, 0], [1,2]],
	'2': [[0, 0], [2, 0], [2, 1], [0, 1], [0, 2], [2, 2]],
	'3': [[0, 0], [2, 0], [2, 1], [0, 1], [2, 1], [2, 2], [0, 2], PEN_OFF],
	'4': [[0, 0], [0, 1], [2, 1], [2, 0], [2, 2]],
	'5': [[0, 0], [2, 0], [0, 0], [0, 1], [2, 1], [2, 2], [0, 2]],	
	'6': [[0, 0], [2, 0], PEN_ON, [0, 0], [0, 2], [2, 2], [2, 1], [0, 1], PEN_OFF, [2, 2]], 
	'7': [[0, 0], [2, 0], [2, 2], PEN_OFF], 
	'8': [[0, 0], [2, 0], [2, 1], [0, 1], [0, 2], [2, 2], [2, 1], [0, 1], [0, 0], PEN_OFF, [0, 2]], 
	'9': [[2, 1], [0, 1], [0, 0], [2, 0], [2, 2]], 
	'0': [[0, 0], [0, 2], [2, 2], [2, 0], [0, 0], [2, 2], PEN_OFF],
	'A': [[0, 0], [2, 0], [2, 2], PEN_OFF, [0, 0], PEN_ON, [0, 2], PEN_OFF, [0, 1], PEN_ON, [2, 1], PEN_OFF, [2, 2]],
	'B': [[0, 0], [2, 0], [1, 1], PEN_OFF, [0, 0], PEN_ON, [0, 2], [2, 2], [2, 1], [0, 1], PEN_OFF],
	'C': [[2, 0], [0, 0], [0, 2], [2, 2]],
	'D': [[2, 1], [2, 2], [0, 2], [0, 0], [2, 1]],
	'E': [[0, 0], [2, 0], PEN_OFF, [0, 0], [0, 1], [2, 1], PEN_OFF, [0, 1], PEN_ON, [0, 2], [2, 2]],
	'F': [[2, 0], [0, 0], [0, 2], [0, 1], [2, 1]],
	'G': [[2, 0], [0, 0], [0, 2], [2, 2], [2, 1], [1, 1]],
	'H': [[0, 0], [0, 2], PEN_OFF, [2, 0], PEN_ON, [2, 2], [2, 1], [0, 1]],
	'I': [[1, 0], [1, 2]],
	'J': [[1, 0], [2, 0], [2, 2], [0, 2], [0, 1]],
	'K': [[0, 0], [0, 2], [0, 1], [2, 0], [0, 1], [2, 2]],
	'L': [[0, 0], [0, 2], [2, 2]],
	'M': [[0, 0], [0, 2], PEN_OFF, [2, 2], PEN_ON, [2, 0], [1, 1], [0, 0]],
	'N': [[0, 0], [0, 2], PEN_OFF, [2, 0], PEN_ON, [2, 2], [0, 0]],
	'O': [[0, 0], [0, 2], [2, 2], [2, 0], [0, 0]],
	'P': [[0, 0], [0, 2], PEN_OFF, [0, 0], PEN_ON, [2, 0], [2, 1], [0, 1]],
	'Q': [[0, 0], [0, 2], [2, 2], [2, 0], [0, 0], PEN_OFF, [2, 2], PEN_ON, [1, 1]],
	'R': [[0, 0], [0, 2], PEN_OFF, [2, 2], PEN_ON, [1, 1], PEN_OFF, [0, 0], PEN_ON, [2, 0], [2, 1], [0, 1]],
	'S': [[0, 0], [2, 0], [0, 0], [1, 1], [2, 1], [1, 2], [0, 2]],
	'T': [[0, 0], [2, 0], [1, 0], [1, 2]],
	'U': [[0, 0], [0, 2], [2, 2], [2, 0]],
	'V': [[0, 0], [1, 2], [2, 0]],
	'W': [[0, 0], [0, 2], [1, 1], [2, 2], [2, 0]],
	'X': [[0, 0], [2, 2], PEN_OFF, [0, 2], PEN_ON, [2, 0]],
	'Y': [[0, 0], [1, 1], [2, 0], [1, 1], [1, 2]],
	'Z': [[0, 0], [2, 0], [0, 2], [2, 2]],
	' ': [],
	'_': [[0, 2], [2, 2]],
	'\n': ["WRAP"],
	'?': [[0,0],[2,0],[2,1],[1,1],PEN_OFF],
	'.': [[0,2], DOT],
	'@':[[1,1], [2,0], [2, 1], [1, 2], [0, 1], [0,0], [1,1]]
}

def instruction_handler(instruction,location = (0,0)):
	if instruction == PEN_ON:
		print PEN_ON
		turtle.pendown()

	elif instruction == PEN_OFF:
		print PEN_OFF
		turtle.penup()
	elif instruction == DOT:
		turtle.dot()

	elif isinstance(instruction, list) or isinstance(instruction, tuple):
		print "GOTO LOCATION"
		print 'x:{}\ty:{}'.format(instruction[0], instruction[1])
		x, y = list(map(scale, instruction))

		x = locationScale(-x,location[0])
		y = locationScale(y,location[1])

		turtle.goto(x, y)
	else:
		raise Exception
def sentenceWrite(strr, starting_pos = [0, 0]):
	strr = strr.upper()
	for letter, letter_pos in zip(strr, range(len(strr))):

		instruction_handler(PEN_OFF)

		for instruction in letters[letter]:
			instruction_handler(instruction, (posistion(letter_pos)+ starting_pos[0],0+ starting_pos[1]))

			if letters[letter].index(instruction) == 0:
				instruction_handler(PEN_ON)

		instruction_handler(PEN_OFF)

	

turtle.speed(0)
turtle.ht()
turtle.pensize(3)
turtle.delay(0)
try:
	sentenceWrite(raw_input("String: "), (-600, -150))
except:
	pass
sentenceWrite("Hello Mr. heldman my name is mike firestack.", (-600, 0))
sentenceWrite("0123456789.",(-600, -50))
sentenceWrite("The quick brown fox jumped over the lazy dog.",(-600, -100))

turtle.mainloop()