__author__ = 'root'



#Return the closest prime higher than the argument
def closest_higher_prime(number):
    number += 1
    while not is_prime(number):
        number+=1
    return number


#Return whether the number is prime
def is_prime(number):

    for x in range(2, number):
        if number%x == 0:
            return False
    return True
#Currently highest found prime
highest_prime = 2

#Set highest found prime if the number is actually higher
def set_highest_prime(number):
    global highest_prime
    if number>2:
        highest_prime = number

#Curenny remainder
remainder = None

#Recursively get the prime factors
def prime_factor(number):

    global remainder
    global highest_prime

    if remainder != 1:
        if number%highest_prime==0:
            remainder = number//highest_prime

        else:
            remainder = number
            highest_prime = closest_higher_prime(highest_prime)

        prime_factor(remainder)


#Print the highest prime factor in the argument
def print_highest_prime(number):
    prime_factor(number)

    print("Highest Prime Factor: " + str(highest_prime))

print_highest_prime(600851475143)