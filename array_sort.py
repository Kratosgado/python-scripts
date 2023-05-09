double_array = [
    [4,6,8],
    [3,2,9],
    [5,1,7]
]

def checkSwap(first, second):
    if (first > second):
        return second, first
    return first, second


def sort(arr):
    oneD = []
    sorted = []
    counter = 0
    for row in arr:
        for index in row:
            oneD.append(index)
    print(oneD)

    counter = 0
    low = 10
    for index in range(len(oneD)):
        for num in range(len(oneD)):
            if (oneD[num] < low):
                oneD.remove[num]
        sorted.append(low)
    return sorted
        
print(sort(double_array))