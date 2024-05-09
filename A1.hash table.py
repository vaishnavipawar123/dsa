n = int(input("Enter number of clients: "))
clients = []
name = []
m = int(input("Enter table size: "))

for k in range(100):
	clients.append(' ')
	name.append(' ')

def linear():
	for i in range(n):
		no  = int(input("Enter telephone number of client for linear hashing: "))
		nav = input("Enter name of client for linear hashing: ")
		key = no%m
		temp = key
		if(clients[key] == ' '):
			name[key] = nav
			clients[key] = no
		else:
			while(1):
				if(clients[temp] != ' '):
					if(temp == m-1):
						temp = 0
					else:
						temp = temp + 1
				else: 
					name[temp] = nav
					clients[temp] = no
					break

def display():
	for j in range(m):
		print(j," |", name[j],"|",  clients[j])
		
def search():
	searchTel = int(input("Enter number of the client: "))
	h = searchTel%m
	temp = h
	counter = 0
	if(clients[temp] == searchTel):
		counter = counter + 1
		print("Number found at index: ", temp, "name of client is: ",name[temp])
		print("Number of comparison required to search required telephone number is: ",counter)
	else:
		counter = counter + 1
		while(1):
				if(clients[temp] != searchTel):
					counter = counter + 1
					if(temp == m-1):
						temp = 0
					else:
						temp = temp + 1
				else: 
					print("Number found at index: ", temp, "name of client is: ",name[temp])
					print("Number of comparison required to search required telephone number is: ",counter)
					break
	
clients1 = []
name1 = []

for k in range(100):
	clients1.append(' ')
	name1.append(' ')

def display1():
	for z in range(m):
		print(z," |", name1[z],"|",  clients1[z])

def double():
	for i in range(n):
		no  = int(input("Enter telephone number of client for double hashing: "))
		nav = input("Enter name of client for double hashing: ")
		key = no%m
		h3 = key
		if(clients1[key] == ' '):
			name1[key] = nav
			clients1[key] = no
		else:
			point = 0
			while(1):
				if(clients1[h3] != ' '):
					point = point + 1
					h2 = 7 - (no%7)
					h3 = (key + (point * h2))%m
				else:
					name1[h3] = nav
					clients1[h3] = no
					break

def search1():
	searchTel = int(input("Enter number of the client: "))
	h = searchTel%m
	temp = h
	counter = 0
	if(clients1[temp] == searchTel):
		counter = counter + 1
		print("Number found at index: ", temp, "name of client is: ",name1[temp])
		print("Number of comparison required to search required telephone number is: ",counter)
	else:
		counter = counter + 1
		point = 0
		while(1):
				if(clients1[temp] != searchTel):
					counter = counter + 1
					point = point + 1
					h2 = 7 - (searchTel%7)
					temp = (h + (point * h2))%m
				else: 
					print("Number found at index: ", temp, "name of client is: ",name1[temp])
					print("Number of comparison required to search required telephone number is: ",counter)
					break

def main():
	while(1):
		print("\n")
		print("YOUR CHOICES ARE")
		print("\n1. Linear Hashing \n2. Search (Linear hash) \n3. Double Hashing \n4. Search (Double Hash) \n5. Exit")
		n = int(input("Enter your choice: "))
		if(n == 1):
			linear()
			display()
		elif(n == 2):
			search()
		elif(n == 3):
			double()
			display1()
		elif(n == 4):
			search1()
		elif(n == 5):
			exit(0)
		elif(n<0 and n>5):
			print("Enter valid choice!!!")
main()