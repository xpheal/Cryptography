# Program that find prime factors iff next (perfect square - N) is a perfect square
import gmpy2
import sys
from gmpy2 import mpz

n = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
# n = mpz('3405971539559')

if gmpy2.is_square(n):
	sqrt = gmpy2.isqrt(n)
else:
	sqrt = gmpy2.isqrt(n)
	sqrt += 1

nsquare = gmpy2.mul(sqrt, sqrt)

print "Next perfect square:\n" + nsquare.digits(10)

diff = n - nsquare

if diff < 0:
	diff = -diff

print "Diff:\n" + diff.digits(10)

if gmpy2.is_square(diff):
	print "Diff is a perfect square"
else:
	print "Diff is not a perfect square"
	sys.exit()

sqrtDiff = gmpy2.isqrt(diff)

p = sqrt - sqrtDiff
q = sqrt + sqrtDiff

print "p = " + p.digits(10)
print "q = " + q.digits(10)

ans = gmpy2.mul(p, q)

if ans == n:
	print "Answer is correct"
	print "N is " + ans.digits(10)
else:
	print "Something's wrong, answer is not correct"
