for I in range(100):
	if I %3 == 0 and I % 5 == 0:
		print(“fizz buzz”)
	elif I % 3 == 0:
		print(“fizz”)
	elif I % 5 == 0:
		print(“buzz”)
	else:
		print(“”    )