while True:
	alt=int(input("Enter Altitude of plane: "))
	if alt<=1000:
		print("Safe to Land!")
		break
	elif alt<=5000:
		print("Bring down to 1000!")
		continue
	elif alt>5000:
		print("Turn Around and try later!")
		continue