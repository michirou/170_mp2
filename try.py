import random
def change_upto_two_values_generator():
	
	# INSERT CODE HERE
	# Hints:
	count = 0 
	while count<10:
		count += 1
		rand_num = (1,2)
		rand_val = random.choice(rand_num)
		# rand_val = random.choice(rand_num)

		print("rand val", rand_val)
		# count = 0
		# for i in range(2):

		if rand_val==2:
			print("\t generating...")
			var = random.choice(list([2,3]))			
			value = random.choice(list([0,1]))		

						
			var1 = random.choice(list([2,3]))			
			value1 = random.choice(list([0,1]))		
			
			print("\t generating...")
			yield value
			yield value1

		else:
			print("\t generating 1 value...")
			var = random.choice(list([2,3]))			
			value = random.choice(list([0,1]))
			yield value


g = change_upto_two_values_generator()
while True:
	print(next(g))

