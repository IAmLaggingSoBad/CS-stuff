def AND(A,B):
	if A == 1 and B == 1:
		output = 1
	else:
		output = 0
	print("The output is: %d" % output)

def NAND(A,B):
	if A == 1 and B == 1:
		output = 0
	else:
		output = 1
	print("The output is: %d" % output)

def OR(A,B):
	if A == 1 and B == 1:
		print("1")
	else:
		output = 0
	print("The output is: %d" % output)

def XOR(A,B):
	if A != B:
		output = 1
	else:
		output = 0
	print("The output is: %d" % output)

def NOR(A,B):
	if A == 0 and B == 0:
		output = 1
	elif A == 0 and B == 1:
		output = 0
	elif A == 1 and B == 0:
		output = 0
	elif A == 1 and B == 1:
		output = 0
	print("The output is: %d" % output)

def XNOR(A,B):
	if A == B:
		output = 1
	else:
		output = 0
	print("The output is: %d" % output)

def choice():
	temp = input("Which logic gate would you like to perform on: \n1. AND \n2. NAND \n3. OR \n4. XOR \n5. NOR \n6. XNOR \n[1/2/3/4/5/6]: ")
	if temp not in ("1", "2", "3", "4", "5", "6"):
		print("Input a number 1 to 6 \n")
		choice()
	elif temp == "1":
		AND(A,B)
	elif temp == "2":
		NAND(A,B)
	elif temp == "3":
		OR(A,B)
	elif temp == "4":
		XOR(A,B)
	elif temp == "5":
		NOR(A,B)
	elif temp == "6":
		XNOR(A,B)

while True:
	A = int(input("Please input your A value \n[1/0]: "))
	B = int(input("Please input your B value: \n[1/0]: "))
	if A < 0 or A > 1 or B < 0 or B > 1:
		print("Please enter either 1 or 0")
	else:
		choice()	