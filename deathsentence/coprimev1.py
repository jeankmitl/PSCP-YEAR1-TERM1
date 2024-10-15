"""CoPrimeV1"""
def main():
    """from the screen to the ring to the pen to the king :fire:"""
    first = int(input())
    second = int(input())
    total = 1
    base = 2
    if min(first,second)<=0:
        print(max(first,second))
        return
    while True:
        if base > min(first,second):
            break
        if not( first%base or second%base):
            first /= base
            second /= base
            total *= base
        else:
            base += 1
    if total in (1,7):
        print('YES')
        print(total)
        return
    print('NO')
    print(total)
main()
