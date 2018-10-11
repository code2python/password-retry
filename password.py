p = 3
while True:
	password = input('Please enter password: ')
	if password == 'a123456':
		print('Login successfully!!')	
		break
	else:
		p = p - 1
		print('password incorrect!! You have:', p,'attempts')
		if p == 0:
			break
			
