while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        
def isPalindrome(n):
    temp = n            # store number in a temporary variable
    reversed_number = 0
    while n:
        reversed_number = reversed_number * 10 + (n % 10)
        n //= 10
    return temp == reversed_number

print(isPalindrome(number))