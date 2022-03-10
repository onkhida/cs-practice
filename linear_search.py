import random
mylist = [random.randint(0, 10) for i in range(10)]

n = int(input("what number are you trying to find? "))

print(mylist)
print(n)
for i in range(len(mylist)):
    if mylist[i] == n:
        print("This has been found")

    else:
        print("nothing for you bastard")