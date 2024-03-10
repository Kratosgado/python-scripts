#a function to find the average of n number of students

#recieve the number of students whose average age is to be calculated
num = int(input('How many students are you going to work with: '))
def ave(n):
	sum = 0
	for i in range(n):
		age = int(input('Enter the age: '))
		
		sum += age
	average = sum/n
	return 'The average of the ages is: ' , average
    
print(ave(num))