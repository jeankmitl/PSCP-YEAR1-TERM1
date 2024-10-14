'''diamond'''
def main():
    'dont mine at night'
    size = int(input())
    space = ' '
    sta = '*'
    middle = (size + 1 // 2) + 1
    middle2 = middle//2
    for j in range(1, middle):
        out = middle2 - j
        if j == middle//2:
            break
        if j == 1:
            print((space * out) + sta + (space * out))
        else:
            print((space * out) + sta + (space * (j-1))  + (space * (j-2))  + sta + (space*(j-2)))
    print(sta * size)
main()
