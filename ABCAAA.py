# given A, B, C are integers not null,
# find AB * C = AAA, 

for ab in range(10, 100):
	for c in range(1, 10):
		product = str(ab*c)
		try:
			if(product[0] == str(ab)[0] and (product[0] == product[1] and product[1] == product[2])): 
				print(f'ab: {ab}\nc: {c}\nab*c: {ab*c}')
		
		except:
			pass




