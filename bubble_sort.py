import random

random_arr = [random.randint(1,100) for i in range(10)]

def bubble_sort(arr):
    arr_length = len(arr)
    
    # iterate through the array a certain number of times
    for i in range(arr_length):

        print(arr_length-i-1)
        for k in range(i-arr_length-1):
            # if the left element is bigger than the right
            if arr[k] > arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
                #swap them

print(random_arr)
print(bubble_sort(random_arr))