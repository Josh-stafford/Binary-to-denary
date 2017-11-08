def unsigned(number):
	num = number[::-1]
	converted = 0
	for n in range(len(num)):
		converted += int(num[n]) * 2**n
	return converted

def sam(number):
	num = number[::-1]
	converted = 0
	msb = num[(len(num))-1]
	num = num[:-1]
	for n in range(len(num)):
		converted += int(num[n]) * 2**n
	if msb == '1':
		converted *= -1
	return converted

def tc(number):
	num = number[::-1]
	converted = 0
	msb = num[(len(num))-1]
	for n in range(len(num)-1):
		converted+= int(num[n]) * 2**n
	if msb == '1':
		converted = (-1*(2**int(len(num)-1))) + converted
	return converted

