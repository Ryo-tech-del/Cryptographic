def garake(PLAIN):
	enc=""
	for chr in list(PLAIN):
		num=ord(chr)
		num=num-97
		first_num=(num+2)//3+1
		second_num=num%3+1
		enc+=str(first_num)
		enc+=str(second_num)
		enc+=" "
	
	print(enc)
