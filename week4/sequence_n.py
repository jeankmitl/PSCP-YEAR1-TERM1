'''i love sequence n'''
def main():
    '''print n'''
    size = int(input())
    for i in range(size):
        for j in range(size):
            if j in (i, size - 1, 0):
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
