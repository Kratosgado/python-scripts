nums: list = []
while True:
    try:
        number = input("Please enter number: ")
        if number == "":
            break
        nums.append(int(number))
    except ValueError:
        print("Oops! That was not a valid number. Try again...")

def findLargest(nums: list):
    largest = -13894
    for i in nums:
        largest = i if i > largest else largest
    return largest

print(findLargest(nums=nums))