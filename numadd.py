try:
	number = int(input("Enter number between 0 to 999 : "))
	if number < 1000 :
	
		h = number//100
		o = number % 10
		t = number-(h*100) - o
		t1 = t/10
		total =int(h+o+t1)
		print(total)

	else:
		print("Please enter number less than 1000")
except ValueError:
	   print("Please enter number only")
