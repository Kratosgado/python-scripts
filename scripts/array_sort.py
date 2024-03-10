double_array = [
    [4,6,8],
    [3,2,9],
    [5,1,7]
]


def sort(arr):
    oneD = []
    sorted = []
    counter = 0
    for row in arr:
        for index in row:
            oneD.append(index)
    print(oneD)

    counter = 0
    for index in range(len(oneD)):
        low = 10
        for num in range(len(oneD)):
            print(len(oneD))
            print("iteration ", num)
            if (oneD[num] < low):
                low = oneD[num]
        sorted.append(low)
    return sorted
        
print(sort(double_array))