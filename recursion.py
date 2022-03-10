# recursion practice
def lettersbackward(n):
    print(chr(n+64))

    if n > 0:
        lettersbackward(n-1)


lettersbackward(70)