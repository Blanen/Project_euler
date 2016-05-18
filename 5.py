__author__ = 'root'
"""An inefficient working solution. I can think of a more efficient solution with prime trees... But, would have to spend more time on it"""

i = 0
found = 0
divisors = 20

primes = []

while True:
    for x in range(2, divisors + 1):
        if i%x != 0:
            break
        if x == divisors:
            found = i
            break
    if found != 0:
        break
    i += 1

print("Answer is: " + str(found))
