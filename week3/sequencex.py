'''WAAAAH'''
def pain(n):
    '''wowie'''
    for i in range(1, n+1):
        print("   " * (n - i), end="")
        for j in range(1, i+1):
            print(f"{j:02d}", end=" ")
        for j in range(i-1, 0, -1):
            print(f"{j:02d}", end=" ")
        print()
    for i in range(n-1, 0, -1):
        print("   " * (n - i), end="")
        for j in range(1, i+1):
            print(f"{j:02d}", end=" ")
        for j in range(i-1, 0, -1):
            print(f"{j:02d}", end=" ")
        print()
pain(int(input()))
