#Fruit shop project:
#Implement using dictionary
#	-Add fruit
#	-Delete fruit by name
#	-Search fruit by name and rate
#	-Change fruit name and rate
#	-Add to cart(List the fruits with fruit_id->select id->store in cart list)
#	-Display
#Properties: fruit_id,fruit_name,rate,imported_from,import_date,buy_price

cart_list = []
fruitsshop = {}
while True : 
	print("1. Add fruit")
	print("2. Delete fruit by name")
	print("3. Search fruit by name and rate")
	print("4. Change fruit name and rate")
	print("5. Add to cart")
	print("6. Display")
	print("7. Display Cart")
	print("8. Exit")
	ch = int(input("Enter the choice"))
	if ch == 1 :
		print("*****Add fruit*****")
		fruitd = int(input("Enter fruit id"))
		if fruitd not in fruitsshop.keys():
			fruit_name = input("Enter fruit name")
			rate = input("Enter rate")
			imported_from = input("Enter the place")
			import_date = input("Enter the imported date")
			buy_price = input("Enter the buy price")
			fruit = {
				"fruit_name" : fruit_name,
				"rate" : rate,
				"imported_from" : imported_from,
				"import_date" : import_date,
				"buy_price" : buy_price
				}
			fruitsshop[fruitd] = fruit
			print("Fruit Details Added")
	elif ch == 2 :
		print("*****Delete fruit by name*****")
		fruitid = int(input("Enter fruit id"))
		name = input("Enter fruit name")
		flag = False
		if fruitid in fruitsshop.keys():
			for frdet in fruitsshop.values():
				if frdet["fruit_name"] == name :
					flag = True
		else:
			print("Enter valid ID")
		if flag == True:
			del fruitsshop[fruitid]
	elif ch == 3:
		print("*****Search fruit by name and rate*****")
		fruitid = int(input("Enter fruit id"))
		if fruitid in fruitsshop.keys():
			print("\t a. Search by name")
			print("\t b. Search by rate")
			choice = input("\tEnter the choice")
			flag = False
			if choice == "a":
				name = input("\tEnter the name")
				for frdet in fruitsshop.values():
					if frdet["fruit_name"] == name :
						flag = True
				if flag == True:
					print(f"\t{fruitid} : {name} is found")
				else:
					print(f"\t{name} is not found")
			elif choice == "b":
				rate = input("\tEnter the rate")
				for frdet in fruitsshop.values():
					if frdet["rate"] == rate :
						flag = True
				if flag == True:
					print(f"\t{fruitid} : {rate} is found")
				else:
					print(f"\t{rate} is not found")
			else:
				print("Wrong Choice")
	elif ch == 4:
		print("*****Change fruit name and rate*****")
		fruitid = int(input("Enter fruit id"))
		if fruitid in fruitsshop.keys():
			print("\t a. Update by name")
			print("\t b. Update rate ")
			choice = input("\tEnter the choice")	
			if choice == "a":
				new_name = input("\tEnter the fruit name to be change")
				fruitsshop[fruitid]["fruit_name"] = new_name
			elif choice == "b":
				new_rate = input("\tEnter the fruit rate to be change")
				fruitsshop[fruitid]["rate"] = new_rate
			else:
				print("Wrong Choice")
		else:
			print("ID is not present")
	elif ch == 5:
		print("*****Add to cart Function*****")
		print(fruitsshop)for fid,values in fruitsshop.items():
			print(f"{fid} : {values}\n")
		print("\t a. Add to Cart")
		print("\t b. Display Cart")
		choice = input("\tEnter the choice")
		if choice == "a":
			num = int(input("\tEnter the fruitid to add"))
			if num in fruitsshop.keys():
				cart_list.append(num)
			else:
				print("\tInvalid ID")
		elif choice == "b":
			print(cart_list)
			for i in cart_list:
				print(f"{i} : {fruitsshop[i]}\n")
		else:
			print("\tInvalid Choice")
	elif ch == 6:
		print("*****Display*****")
		for fid,values in fruitsshop.items():
				print(f"{fid} : {values}\n")
	elif ch == 7:
		print("*****Display Cart*****")
		for i in cart_list:
			print(f"{i} : {fruitsshop[i]}\n")
	elif ch == 8:
		print("Exit")
		break
	else:
		print("Invalid choice")
	
