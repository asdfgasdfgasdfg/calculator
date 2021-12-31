def listToEquation(someList):
    answerString = ""
    for x in range(0,len(someList)):
        if someList[x] == 0: #if coefficient is 0, skip the term
            continue
        elif someList[x] > 0 and x!=0: #if 1 or -1, add a plus or minus, unless positive first term
        	answerString += "+ "
        elif someList[x] < 0:
        	answerString += "- "

        if someList[x] == 1:
        	pass
        elif someList[x]>0: #if coefficient is positive, print the coefficient
            answerString += str(someList[x])
        elif someList[x]<0: #if coefficient is negative, make it positive
            answerString += str(someList[x]*-1)

        if x == len(someList) - 2: #if degree is 1, add an x
            answerString += "x "
        elif x != len(someList) - 1: #if degree isn't 0, add an x^degree
            answerString += "x^"+str(len(someList)-1-x)+" "

    return answerString

a = int(input("Degree: "))
b = []
for x in range(0,a+1):
    b.append(float(input("Coefficient of x^"+str(a-x)+": ")))

while True:
	print("\n--Enter -1 to quit--")
	a = int(input("Degree:"))
	if a == -1:
		break
	c = []
	for x in range(0,a+1):
	    c.append(float(input("Coefficient of x^"+str(a-x)+": ")))

	ans = []
	for x in range(0,len(b)+len(c)-1):
		ans.append(0)

	for x in range(0,len(b)):
		for y in range(0,len(c)):
	b = ans
	print(listToEquation(b))