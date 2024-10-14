'''harshat the toilet'''
def summary(num):
    '''usmma'''
    snum = 0
    if num < 0:
        for i in (str(num))[1:]:
            snum += int(i)
        snum *= -1
    else:
        for i in str(num):
            snum += int(i)
    return snum
def main():
    """Harshad"""
    for _ in range(10):
        num = int(input())
        if not num:
            print("No")
        elif len(str(num)) == 1:
            if not num % num:
                print("Yes")
            else:
                print("No")
        else:
            if not num % summary(num):
                print("Yes")
            else:
                print("No")
main()
