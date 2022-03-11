import random 

random_arr = [random.randint(0,100) for i in range(10)]

def insertion_sort(arr):
    for i in range(1, len(arr) - 1):

        while arr[i-1] > arr[i] and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1] 
            # swap the elements of arr
            i = i-1

    return arr

print(random_arr)
print(insertion_sort(random_arr))