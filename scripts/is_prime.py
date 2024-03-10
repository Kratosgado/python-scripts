while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

def is_prime(n):
    # check if n is less than 2
    if n < 2:
        return False
    for i in range(2, n):
        # check if n is divisible by any number between 2 and n
        if n % i == 0: 
            return False
    return True

print(is_prime(number))