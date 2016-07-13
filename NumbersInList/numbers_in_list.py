def main():
	return

def add_ONE(ls, num):
	if len(ls) == 0:
		return [num]
	
	check = True
	for i in range(len(ls)):
		index = len(ls) - i - 1
		last_sum = ls[index] + num
		if last_sum < 10:
			ls[index] = last_sum
			check = False
			break
		ls[index] = last_sum % 10

	if check == True:
		ls = [1] + ls

	return ls

def add_generic_nr(ls, num):
	if len(ls) == 0:
		return [num] 
	
	add_one = True
	for index in range(len(ls)-1, -1, -1):
		last_sum = ls[index] + num if index == len(ls)-1 else ls[index] + 1
		if last_sum < 10:
			ls[index] = last_sum
			add_one = False
			break
		ls[index] = last_sum % 10

	if add_one:
		ls = [1] + ls

	return ls






if __name__ == '__main__':
	main()










