'''pro'''
def main():
    '''pro'''
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())

    promotion = (z // x) * y
    no = z % x
    total = (promotion + no) * a

    print(total)
main()
