def reverse_number(num):
	rev_num = 0
	while num != 0:
		digit = num % 10
		rev_num = rev_num * 10 + digit
		num  = num // 10
	print("reversed number is:",rev_num)		


num = int(input("Enter the number:"))
reverse_number(num)
