__author__ = 'root'

"""Iterative fibonacci function where the parameter is the maximum number and returns the sum of all the even number of
the numbers up till then.
You might ask, why not recursive? Because it was slow and I had to look up that you needed to make do tail call
optimalization and if I did that, I would have felt like cheating."""

def sums_fib_even(maximum):
    a = 0
    b = 1
    even_sums = 0

    while True:
        sumxy = a + b

        if(sumxy > maximum):
            break

        a = b
        b = sumxy

        if b%2==0:
            even_sums+=b

    return even_sums

print (sums_fib_even(4000000))