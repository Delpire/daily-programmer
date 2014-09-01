def select_range(range_to_select):

	selection = []

	beginning_x = convert_to_decimal(range_to_select[0][0])
	beginning_y = int(range_to_select[0][1]) - 1
	ending_x = convert_to_decimal(range_to_select[1][0])
	ending_y = int(range_to_select[1][1:]) - 1

	#print(beginning_x)
	#print(beginning_y)
	#print(ending_x)
	#print(ending_y)

	for x in range(beginning_x, ending_x + 1):
		for y in range(beginning_y, ending_y + 1):
			selection.append([x, y])

	#print(selection)

	return selection


def select(input):

	selection = []

	groups = input.split('&')

	for group in groups:

		to_select = group.split(":")

		if len(to_select) > 1:
			selection = selection + select_range(to_select)

		else:
			x = convert_to_decimal(to_select[0][0])
			y = int(to_select[0][1]) - 1
			selection.append([x, y])

	return selection

def deselect_range(range_to_deselect, selection):
	beginning_x = convert_to_decimal(range_to_deselect[0][0])
	beginning_y = int(range_to_deselect[0][1]) - 1
	ending_x = convert_to_decimal(range_to_deselect[1][0])
	ending_y = int(range_to_deselect[1][1]) - 1

	for x in range(beginning_x, ending_x + 1):
		for y in range(beginning_y, ending_y + 1):
			if [x, y] in selection:
				selection.remove([x, y])

	return selection

def deselect(input, selection):
	
	groups = input.split('&')

	for group in groups:

		to_deselect = group.split(":")

		if len(to_deselect) > 1:
			selection = deselect_range(to_deselect, selection)

		else:
			x = convert_to_decimal(to_deselect[0][0])
			y = int(to_deselect[0][1]) - 1
			if [x, y] in selection:
				select = selection.remove([x, y])

	return selection

def  parse_by_except(input):

	parsed_input = input.split('~')

	selection = select(parsed_input[0])

	if len(parsed_input) > 1:
		selection = deselect(parsed_input [1], selection)

	for sel in selection:
		print(sel)

def convert_to_decimal(base_twenty_six):
	
	base_twenty_six.upper()
	
	result = 0

	for char in base_twenty_six:
		result *= 26
		result += ord(char) - 64

	return result - 1

parse_by_except('B1:B3&B4:E10&F1:G1&F4~C5:C8&B2')