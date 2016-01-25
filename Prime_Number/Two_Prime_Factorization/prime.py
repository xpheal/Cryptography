# Program to find semi prime factors based on question3 of Project2
import gmpy2
from gmpy2 import mpz
import sys

def proot(a, b, c):
	tr = gmpy2.mul(b, b)
	ac = gmpy2.mul(a, c)
	tr -= gmpy2.mul(ac, 4)
	tr = gmpy2.isqrt(tr)
	ta = gmpy2.mul(a, 2)

	# +ve side
	ret1 = b + tr
	ret1 = gmpy2.f_div(ret1, ta)
	if 0 > ret1:
		return -ret1

	# -ve side
	ret2 = b - tr
	ret2 = gmpy2.f_div(ret2, ta)
	if 0 > ret2:
		return -ret2
	else:
		print "proot Error"
		sys.exit()

if len(sys.argv) > 2:
	print "Usage: python prime.py [N]"
	sys.exit()
elif len(sys.argv) == 2:
	n = mpz(str(sys.argv[1]))
else:
	# n = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')

	# small case 1
	# p = 1049, q = 1103
	# n = mpz('1157047')

	# small case 2
	# p = 1459153, q = 1459583
	# n = mpz('2129754913199')

	# small case 3
	# p = 169743212304 q = 169743214699
	n = mpz('28812758529815810456496')
	
m = n

# ceil(x^(1/2))
if gmpy2.is_square(m):
	m1 = gmpy2.isqrt(m)
else:
	m1 = gmpy2.isqrt(m)
	m1 += 1

print "m1= "
print m1.digits(10)

# ceil(x^(1/4))
if gmpy2.is_square(m1):
	m2 = gmpy2.isqrt(m1)
else:
	m2 = gmpy2.isqrt(m1)
	m += 1

print "m2= "
print m2.digits(10)

# 2 * x^(1/4)
dist = gmpy2.mul(m2, 2)

print "dist= "
print dist.digits(10)

# calculate p_max
p_max = m1 + 1
p_max = gmpy2.mul(p_max, 2)

print "p_max= "
print p_max.digits(10)

# calculate p_min
p_min = proot(1, dist, -(n - 1))

print "p_min= "
print p_min.digits(10)

# start finding prime
if gmpy2.is_prime(p_min):
	p = p_min
else:
	p = gmpy2.next_prime(p_min)

# loop through prime numbers from p_min to p_max
while p < p_max:
	# get remainder of div(n, p)
	rem = gmpy2.t_mod(n, p)

	if rem == 0:
		print "\nresult= "
		print "p= "
		print p.digits(10)
		print "q= "
		print gmpy2.c_div(n, p)
		sys.exit()

	p = gmpy2.next_prime(p)

