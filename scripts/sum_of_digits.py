while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        
def sum_of_digits(n):
    sum = 0
    while n:            # while n != 0
        sum += n % 10   # sum = sum + n % 10 : modulo
        n //= 10        # n = n // 10 : floor division
    return sum

print(sum_of_digits(number))