'''mrwhite'''
def asc(x, y):
    '''gay'''
    if not x % 2:
        x += 1
    if not y % 2:
        y += 1
    for i in range(x-2, y, 2):
        i += 1
        print(i, end=' ')
def dsc(x, y):
    '''gay'''
    if not x % 2:
        x += -1
    if not y % 2:
        y += 2
    for i in range(x, y-2, -2):
        i += -1
        print(i, end=' ')
def main():
    '''bruh'''
    start = int(input())
    finish = int(input())
    if start >= finish:
        print(f"pass : {dsc(start, finish)}")
        print(f"pass : {dsc(start, finish)}")
    else:
        print(f"pass : {asc(start, finish)}")
main()
