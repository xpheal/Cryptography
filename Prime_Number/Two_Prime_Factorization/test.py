import gmpy2
from gmpy2 import mpz

x = mpz('1000000000000000000020000000')
p = mpz('1000000000000000000001000000')

while p < 1000000000000000000010000000:
	if gmpy2.is_prime(p):
		y = gmpy2.t_mod(x, p)

	p = gmpy2.next_prime(p)