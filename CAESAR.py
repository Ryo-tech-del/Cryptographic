def caesar(PLAIN,KEY):
	enc=""
	for char in list(PLAIN):
             ASCII=ord(char)
             num=ASCII-97
             num=(num+KEY)%26
             ASCII=num+97
             enc+=chr(ASCII)
     
	print(enc)




def break_caesar(ENC,KEY):
	plain=""
	for char in list(ENC):
		ASCII=ord(char)
		num=ASCII-97
		num=(num-KEY)%26
		ASCII=num+97
		plain+=chr(ASCII)

	print(plain)
