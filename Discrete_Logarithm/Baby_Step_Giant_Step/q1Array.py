# Baby-Step, Giant-Step algorithm using array
# Complexity of O(p^1/2), trade space for speed
import gmpy2
import sys
from gmpy2 import mpz

# Set maxList to prevent taking up too much space
maxList = 8000000
# maxList = 1000000

# file to save result
f = open('resultArray.txt', 'w')

# Project question
# p = mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
# g = mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
# y = mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')

# Small case 1
# p = mpz('31')
# g = mpz('3')
# y = mpz('6')
# x = 25

# Small case 2
# p = mpz('29')
# g = mpz('2')
# y = mpz('15')
# x = 27

# Small case 3
p = mpz('131071')
g = mpz('478124')
y = mpz('49097')
# x = 28034

# Small case 4
# p = mpz('2147483647')
# g = mpz('1287367342')
# y = mpz('1229665240')
# time taken = 3min
# x = 1953782345

# Small case 5
# p = mpz('56374829353')
# g = mpz('34785642345')
# y = mpz('28183962827')
# time taken: 1hr +
# x = 

# get m, ceiling of sqrt(p)
m = gmpy2.isqrt(p)

if not gmpy2.is_square(p):
	m += 1

# Get inverse of m
invgm = gmpy2.powmod(g, -m, p)

# to track progress
pj = mpz('0')
# pi = mpz('0')

# set up left hand side of comparison
i = 0
leftArray = []

# get iCurr
fi = open('iCurr.txt', 'r')

iCurr = mpz(fi.readline())
fi.close()

# calculate first item 
leftArray.append(gmpy2.powmod(g, iCurr, p))
i += 1

while i < m and i < maxList:
	leftArray.append(gmpy2.t_mod(gmpy2.mul(leftArray[i - 1], g), p))
	i += 1;

# leftArray = []
# leftArray.append(-1)

# right hand side loop
# j = 0
j = 0

i = 0
for left in leftArray:
	if y == left:
		ansEx = gmpy2.mul(m, j) + i
		answer = gmpy2.powmod(g, ansEx, p)

		f.write("p = " + p.digits(10))
		f.write("\ng = " + g.digits(10))
		f.write("\ny = " + y.digits(10))
		f.write("\nm = " + m.digits(10))
		f.write("\nj(right) = " + str(j))
		f.write("\ni(left) = " + str(i))
		f.write("\nanswer = " + ansEx.digits(10))
		f.write("\ncheck g = " + answer.digits(10))
		f.close()
		sys.exit()

	i += 1

# j = 1
j = 1
right = gmpy2.t_mod(gmpy2.mul(invgm, y), p)

for left in leftArray:
	if right == left:
		ansEx = gmpy2.mul(m, j) + i
		answer = gmpy2.powmod(g, ansEx, p)

		f.write("p = " + p.digits(10))
		f.write("\ng = " + g.digits(10))
		f.write("\ny = " + y.digits(10))
		f.write("\nm = " + m.digits(10))
		f.write("\nj(right) = " + str(j))
		f.write("\ni(left) = " + str(i))
		f.write("\nanswer = " + ansEx.digits(10))
		f.write("\ncheck g = " + answer.digits(10))
		f.close()
		sys.exit()

	i += 1

# j = 2
j = 2
rightpow = invgm
while j < m:
	rightpow = gmpy2.t_mod(gmpy2.mul(rightpow, invgm), p)
	right = gmpy2.t_mod(gmpy2.mul(rightpow, y), p)

	i = 0
	for left in leftArray:
		if right == left:
			ansEx = gmpy2.mul(m, j) + i
			answer = gmpy2.powmod(g, ansEx, p)

			f.write("p = " + p.digits(10))
			f.write("\ng = " + g.digits(10))
			f.write("\ny = " + y.digits(10))
			f.write("\nm = " + m.digits(10))
			f.write("\nt = " + str(j))
			f.write("\ns = " + str(i))
			f.write("\nanswer = " + ansEx.digits(10))
			f.write("\ncheck g = " + answer.digits(10))
			f.close()
			sys.exit()

		i += 1

	j += 1

	# print progress
	pj = gmpy2.c_div((j * 100), m)
	print "\r" + pj.digits(10) + " %",

fi = open('iCurr.txt', 'w')
fi.write((iCurr + maxList).digits(10))
fi.close()

fv = open('iValue.txt', 'a')
fv.write((iCurr + maxList).digits(10) + "\n")
fv.close()