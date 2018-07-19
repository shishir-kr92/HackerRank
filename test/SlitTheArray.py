arr = [1,2,3,4,5,6,7,8]

print(arr[0: len(arr): 2])
print(arr[1: len(arr): 2])

evenArray = []
oddArray = []

for i in range(len(arr)):
    if i%2 == 0:
        evenArray.append(arr[i])
    else:
        oddArray.append(arr[i])

print(evenArray)
print(oddArray)
