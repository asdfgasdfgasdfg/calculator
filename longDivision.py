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
        elif x == len(someList) - 1:    #if degree is 0, don't add an x
            answerString += f"{someList[x]} "
        else: #otherwise, add an x^degree
            answerString += f"{someList[x]}x^{len(someList)-1-x} "

    return answerString


a = int(input("Degree of numerator:"))
print("Give the coefficients of the numerator")
b = []
for x in range(0,a+1):
    b.append(float(input("Coefficient of x^"+str(a-x)+": ")))
a = int(input("\nDegree of denominator:"))
print("Give the coefficients of the denominator")
c = []
for x in range(0,a+1):
    c.append(float(input("Coefficient of x^"+str(a-x)+": ")))

# a = 2
# b = [-6, 8, 0, -5]
# c = [3, 1, 8]



d = c.pop(0)
for x in range(0,len(b)-len(c)):
    print(listToEquation(b[x:]))
    w = [-b[x]]
    b[x] /= d
    for i in range(0,len(c)):
        b[x+i+1] -= b[x]*c[i]
        w.append(-b[x]*c[i])
    while len(w) < a-x:
        w.append(0)
    print(listToEquation(w))
    print("---------------------------------")

e = b[-len(c):]

print("Quotient:")
print(listToEquation(b[:-len(c)]))
print("Remainder:")
print(listToEquation(e))