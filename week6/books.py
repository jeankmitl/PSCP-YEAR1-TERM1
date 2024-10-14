'''books'''
from math import ceil
def main():
    '''i don't read books, i need my dopamine hit'''
    book = int(input())
    page = int(input())
    x = int(input())
    y = int(input())
    pages = 0
    days = 0
    count = 0
    while True:
        calpage = ceil((x / y) * page)
        if book == count:
            break
        if calpage >= page:
            break
        pages += calpage
        if pages >= page:
            count += 1
            pages = 0
        x += 1
        y += 1
        days += 1
    days += book-count
    print(days)
main()
