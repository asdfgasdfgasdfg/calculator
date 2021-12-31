class sqrtx:
	"""x is the number inside the sqrt, coNum % coDen is the coefficient numerator 
	and denominator of the sqrt. should be initiated as 1/1 (coNum = 1, coDen = 1)"""
	def __init__(self, x, coNum, coDen, imaginary):
		self.x = x
		self.coNum = coNum
		self.coDen = coDen
		self.imaginary = imaginary
		self.simplify()
		
	def simplify(self):
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
		#deal with negative sqrts
		if self.x < 0:
			self.x *= -1
			if self.imaginary: #if there's already an i, turn it into -1
				self.imaginary = False
				self.coNum *= -1
			else: #if there's no i yet, multiply it by i
				self.imaginary = True
		#decimal to fraction
		while self.coNum%1 + self.coDen%1 != 0:
			self.coNum *= 10
			self.coDen *= 10
		#take out perfect squares, if any, from x and put them in coNum (only checks for prime squares up to 29^2)
		def divide(d, d2, GCD = False):
			if GCD:
				if d%d2 == 0:
					self.coNum/=d2
					self.coDen/=d2
				elif d%d2 != 1:
					divide(d2, d%d2, True)
			elif self.x % d2 == 0:
				self.x /= d2
				self.coNum *= d
				divide(d, d2)

		for i in range(0,len(primes)):
			if self.x < primes[i]**2:
				break #if x is less than the divisor, then it won't be dividable, so quit trying
			divide(primes[i], primes[i]**2)

		#Euclidean GCD algorithm
		if self.coNum>self.coDen:
			big = self.coNum
			small = self.coDen
		else:
			big = self.coDen
			small = self.coNum
		divide(big, small, True)
		#no negative denominators
		if self.coDen < 0:
			self.coNum *= -1
			self.coDen *= -1

	def format(self):
		if self.coDen == 1:
			string = str(self.coNum)
		else:
			string = "("+str(self.coNum) + "/" + str(self.coDen) + ")"
		if self.x != 1:
			string += "√"+str(self.x)+" "
		if self.imaginary:
			string += "i"
		return string

	def multiply(self, sqrtObject):
		#if both imaginary, i*i, i^2 = -1
		params = [self.x, self.coNum, self.coDen, self.imaginary]
		if params[3] and sqrtObject.imaginary:
			params[3] = False
			params[1] *= -1
		elif params[3] or sqrtObject.imaginary: #if one is imaginary, i^1 = 1
			params[3] = True
		#else, they are both real, and params[3] is already initialized as false, so just leave it like that.
		#multiply all the other terms
		params[0] *= sqrtObject.x
		params[1] *= sqrtObject.coNum
		params[2] *= sqrtObject.coDen
		#create sqrt object with parameters and return it
		return sqrtx(params[0], params[1], params[2], params[3])

	def divide(self, sqrtObject):
		params = [self.x, self.coNum, self.coDen, True]
		#divide coefficients by multiplying by the inverse
		params[1] *= sqrtObject.coDen
		params[2] *= sqrtObject.coNum
		#get rid of radicals in the denominator
		params[0] *= sqrtObject.x
		params[2] *= sqrtObject.x
		#if the imaginary parts cancel out
		if self.imaginary == sqrtObject.imaginary:
			params[3] = False
		elif sqrtObject.imaginary: #if the imaginary part is on bottom, multiply by i/i to turn the i into -1
			params[1] *= -1
		return sqrtx(params[0], params[1], params[2], params[3])

def sqrtDiscOver2a(a,b,c):
	discriminant = (b**2 - 4*a*c)
	#if discriminant is negative, imaginary roots
	if discriminant<0:
		discriminant*=-1
		imaginary = True
	else:
		imaginary = False
	return sqrtx(1,2*a,discriminant,imaginary)

coes = []
dgr = 3
"""
dgr = int(input("Degree of polynomial (2-5): "))
for x in range(0,dgr+1):
	coes.append(float(input("Coefficient of x^"+str(dgr-x)+": ")))
"""
#find roots
#for each in roots, (x-root)
#unless root is imaginary or sqrt, then do (x^2 + root^2)
roots = []
#x=y-b/3a
A = (coes[2] - coes[1]**2/(3*coes[0]))/(coes[0])
B = (coes[3]+(2*coes[1]**3)/(27*coes[0]**2)-(coes[1]*coes[2])/(3*coes[0]))/coes[0]
if dgr == 3:
	s = sqrtDiscOver2a(1,B,-(A**3)/27)
	[-B/2+" + "+s.format(), -B/2+" - "+s.format()]
	
	

