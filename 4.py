__author__ = 'root'
"Probably inefficient answer to Problem 4... But it works."

"""Returns Boolean whether argument is a palindrome"""
def is_palindrome(x):

    palindrome_list = []

    x_str = str(x)
    for digit in x_str:
        palindrome_list.append(digit)

    for x in range(0, len(palindrome_list)//2):

        if palindrome_list[x] != palindrome_list[len(palindrome_list)-1-x]:
            return False

    return True

highest_number = 0

"""Set highest_number to the argument if it actually is higher"""
def higher_number(x):
    global highest_number

    if x > highest_number:
        highest_number = x

"""The actual function that iteratates through all the number but doesn't go through the same calculation twice.
Won't do both 101 * 998 AND later 998 * 101"""
def get_highest_palindrome():
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            if is_palindrome(x * y):
                higher_number(x  * y)

    print(highest_number)



get_highest_palindrome()