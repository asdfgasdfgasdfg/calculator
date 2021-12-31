import re

def inputWithFormat(prompt, inputFormat, errorMsg):
	response = input(prompt)
	if re.match(inputFormat, response) != None:
		return response
	else:
		print("\n"+errorMsg)
		return inputWithFormat(prompt, inputFormat, errorMsg)

def getUserData():
	print("Please enter these values as an integer, for example \"5\" for a degree of 5.")
	numeDgr = int(inputWithFormat("What degree is your numerator? ", "^[0-9]+$", "That wasn't an integer. I will ask again."))
	denoDgr = int(inputWithFormat("What degree is your denominator? ", "^[0-9]+$", "That wasn't an integer. I will ask again."))

	numeCoes = []
	print("\nGive the coefficients of the numerator.")
	while numeDgr >= 0:
		numeCoes.append(float(inputWithFormat(f"Coefficient of x^{numeDgr}: ", r"^[+-]?\d+\.?\d*$", "Enter a number. Use 0 if you don't have this term.")))
		numeDgr-=1

	denoCoes = []
	print("\nGive the coefficients of the denominator. The first term must be 1.")
	print(f"Coefficient of x^{denoDgr}: 1")
	denoDgr-=1
	while denoDgr >= 0:
		denoCoes.append(float(inputWithFormat(f"Coefficient of x^{denoDgr}: ", r"^[+-]?\d+\.?\d*$", "Enter a number. Use 0 if you don't have this term.")))
		denoDgr-=1

	#ordered from highest to lowest degree
	return {"nume": numeCoes, "deno": denoCoes}

def listToEquation(someList):
	answerString = ""
	for x in range(0,len(someList)):
		if someList[x] == 0: #if coefficient is 0, skip the term
			continue
		elif x!=0 and someList[x]>0: #if coefficient is positive and it's not the first term, add a + sign
			answerString += "+ "
		elif x!=0 and someList[x]<0: #if coefficient is negative and it's not the first term, move the negative sign to make it look nicer
			answerString += "- "
			someList[x] *= -1
		if someList[x] == 1: #if coefficient is 1, just add the x part, don't add the 1.
			someList[x] = ""

		if x == len(someList) - 2: #if degree is 1, add an x
			answerString += f"{someList[x]}x "
		elif x == len(someList) - 1:	#if degree is 0, don't add an x
			answerString += f"{someList[x]} "
		else: #otherwise, add an x^degree
			answerString += f"{someList[x]}x^{len(someList)-1-x} "

	return answerString

def calculate(numerator, denominator):
	for x in range(0,len(numerator)-len(denominator)):
		for i in range(0,len(denominator)):
			numerator[x+i+1] -= numerator[x]*denominator[i]

	return {"quotient": numerator[:-len(denominator)], "remainder": numerator[-len(denominator):]}

coefficients = getUserData() #{"nume": [-6, 8, 0, -5], "deno": [3, 1, 8]}
answer = calculate(coefficients["nume"], coefficients["deno"])
print(answer)
print(listToEquation(answer["quotient"]))
print(listToEquation(answer["remainder"]))