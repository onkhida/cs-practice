import random 

random_arr = [random.randint(0, 100) for i in range(10)]

def bubble_sort(arr):
    arrlength = len(arr)

    for i in range(arrlength):
        for j in range(0, arrlength-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(random_arr)

x = bubble_sort(random_arr)
print(x)