digits = [1,2,3,4,5,6,7,8,9, 10, 11, 12]

for i in digits:
    if i != 1:
        print(i, end="\t")
    else :
        print("", end="\t")
    for j in digits:
        print(i * j, end="\t")
    print("\n")