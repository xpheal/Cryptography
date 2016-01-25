# Generate 

import gmpy2
from gmpy2 import mpz

p = mpz('2147483647');
g = mpz('1287367342');
x = mpz('1953782345');
ansy = mpz('1229665240');

y = gmpy2.powmod(g, x, p);
print y.digits(10)

if y == ansy:
	print "Correct answer"
else:
	print "Wrong answer"
