n = input('Enter a number: ')

while n.isdigit() == False or int(n) < 1:
	n = input('Please enter a number starting from 1: ')

n = int(n)

n1 = 0
n2 = 1

for _ in range(n):
	print(n2, end=' ')
	n1, n2 = n2, n1 + n2

	

