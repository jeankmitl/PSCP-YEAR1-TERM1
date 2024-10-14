'''sequencemeow'''
def halflifebox(n):
    '''horse'''
    for i in range(1, 2*n):
        for j in range(1, 2*n):
            value = min(i, j, 2*n-i, 2*n-j)
            print(f"{value:02}", end=" ")
        print()
halflifebox(int(input()))
