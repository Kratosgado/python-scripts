while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        
def reverseNumber(n):
    rev_num = 0
    while n:
        rev_num = rev_num * 10 + (n % 10)
        n //= 10        # floor division
    return rev_num

print(reverseNumber(number))