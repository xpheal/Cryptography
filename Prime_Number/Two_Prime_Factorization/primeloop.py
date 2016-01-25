# Naive Approach
import signal
import gmpy2
from gmpy2 import mpz
import sys

p = mpz("-1")

# signal handler
def signal_handler(signal, frame):
	global p
	# p -= 1
	fi = open('pCurr.txt', 'w')
	fi.write(p.digits(10))
	fi.close()

	fv = open('pValue.txt', 'a')
	fv.write(p.digits(10) + "\n")
	fv.close()

	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

n = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')
# n = mpz('2129754913199')

# get p value
fi = open('pCurr.txt', 'r')
p = mpz(fi.readline())
fi.close()

print p.digits(10)

# loop for prime
while p < 14000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
	# get remainder of div(n, p)
	rem = gmpy2.t_mod(n, p)

	if rem == 0:
		q = gmpy2.c_div(n, p)
		f = open('pResult.txt', 'a')
		f.write("p = " + p.digits(10) + "\n")
		f.write("q = " + q.digits(10) + "\n")
		f.write("n = " + n.digits(10) + "\n")
		f.close()

		fi = open('pCurr.txt', 'w')
		fi.write(p.digits(10))
		fi.close()

		fv = open('pValue.txt', 'a')
		fv.write(p.digits(10) + "\n")
		fv.close()
		sys.exit()

	p = gmpy2.next_prime(p)
	# print p.digits(10)