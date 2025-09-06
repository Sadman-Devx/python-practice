def main():
    x = int (input("what's x? "))
    y = int(input("what's y? "))
    print("x square is",square(x),"\ny square is",square(y))
    #print("y square is",square(y))

def square(n):
    return pow(n,2)


main()