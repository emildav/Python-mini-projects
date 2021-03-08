from math import pi

n = ''

while n not in range(1,16):
	try:
		n = int(input('Enter a number (1-15): '))

	except:
		print('Not a number! Please enter a correct number from 1 to 15')

print(round(pi, n))