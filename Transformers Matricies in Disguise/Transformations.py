import math
import re

def convert_input(input):
	return float(input) if '.' in input else int(input)

def translate(coordinates, argument):
	A = convert_input(arguments[0])
	B = convert_input(arguments[1])
	coordinates['X'] = coordinates['X'] + A
	coordinates['Y'] = coordinates['Y'] + B
	return coordinates

def rotate(coordinates, arguments):
	A = convert_input(arguments[0])
	B = convert_input(arguments[1])
	C = convert_input(arguments[2])
	temp_X = math.cos(C) * (coordinates['X'] - A) - math.sin(C) * (coordinates['Y'] - B) + A
	coordinates['Y'] = math.sin(C) * (coordinates['X'] - A) + math.cos(C) * (coordinates['Y'] - B) + B
	coordinates['X'] = temp_X
	return coordinates

def scale(coordinates, arguments):
	A = convert_input(arguments[0])
	B = convert_input(arguments[1])
	C = convert_input(arguments[2])
	Z = math.sqrt((coordinates['X'] - A) ** 2 + (coordinates['Y'] - B) ** 2)
	H = C * Z - Z
	theta = math.acos((coordinates['X'] - A) / Z)
	coordinates['X'] = coordinates['X'] + math.cos(theta) * H
	coordinates['Y'] = coordinates['Y'] + math.sin(theta) * H
	return coordinates

def reflect(coordinates, arguments):

	axis = arguments[0]

	axis = axis.lower()

	if axis == 'x':
		coordinates['X'] = coordinates['X'] * -1
	elif axis == 'y':
		coordinates['Y'] = coordinates['Y'] * -1
	else:
		print("Incorrect input for reflect(). Please enter X or Y.")

	return coordinates

def finish():
	return false;

function_dictionary = {'translate':translate, 'rotate':rotate, 'scale':scale, 'reflect':reflect, 'finish':finish }
coordinates = {'X':0, 'Y':0}

has_no_coordinates = True

while(has_no_coordinates):
	coor_input = input("Enter in a set of coordinates: ") 
	regex_input = re.search('\s*[0-9]+\.?[0-9]*,\s*[0-9]+\.?[0-9]*', coor_input)
	
	if regex_input != None:
		has_no_coordinates = False;
		parsed_input = regex_input.group(0).split(',')
		coordinates['X'] = convert_input(parsed_input[0])
		coordinates['Y'] = convert_input(parsed_input[1])

while(True):
	inp = input("Enter command: ")
	parsed_input = inp.split('(')
	parsed_input[1] = parsed_input[1].replace(")","")
	arguments = parsed_input[1].split(',')

	if parsed_input[0] == 'finish':
		break

	coordinates = function_dictionary[parsed_input[0]](coordinates, arguments)


print(coordinates['X'])
print(coordinates['Y'])
