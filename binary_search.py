from math import floor

# ordered list of 0 to 9 
thearr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tobefound = int(input("what are you looking for? "))

def binary_search(arr, tbf):
    # i want to find the initial indexes for the upper and lower limits

    upper_bound = len(arr) -1
    lower_bound = 0

    found = False

    while found == False:
        # find the midpoint index of the array 
        midpoint = floor((upper_bound + lower_bound) / 2)

        if int(tbf) == arr[midpoint]:
            # if the value to be found is equivalent to the midpoint
            print("You have been found")
            print(midpoint)
            found = True

        elif int(tbf) > arr[midpoint]:
            # if the value to be found is greater than the midpoint
            lower_bound = midpoint + 1
            print("Not yet found")

        elif int(tbf) < arr[midpoint]:
            # if the value to be found is less than the midpoint
            upper_bound = midpoint - 1

        else:
            pass


binary_search(thearr, tobefound)
