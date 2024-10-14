'''chachacha'''
from math import ceil
def main():
    '''im a smoooth criminal'''
    days = int(input())
    total = 0
    i = 0
    while i < days:
        temp = ceil(float(input()))
        total += temp
        i += 1
    print(total * 8720)
main()
