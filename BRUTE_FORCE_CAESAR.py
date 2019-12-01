def Brute_force(ENC):
	KEY=1
	for i in range(25):
		plain=""
		for char in list(ENC):
			ASCII=ord(char)
			num=ASCII-97
			num=(num-KEY)%26
			ASCII=num+97
			plain+=chr(ASCII)
		
		print(plain)
		KEY+=1
