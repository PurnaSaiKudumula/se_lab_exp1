# Version 2 : Keyboard Input:

def Temperature_modeling(a, b, c, time):
	# Example model: quadratic equation for demonstration
	return a * time ** 2 + b * time + c

time = int(input('Enter Time:'))
a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))
temp = Temperature_modeling(a, b, c, time)
print(f"the Temperature at time {time} is {temp}")

