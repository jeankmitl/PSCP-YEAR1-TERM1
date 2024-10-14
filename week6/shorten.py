'''shorten'''
def main():
    '''shorten them balls'''
    result = ""
    start = None
    previous = None
    while True:
        num = int(input())
        if num == -1:
            break
        if start is None:
            start = num
            previous = num
            continue
        if previous != num - 1:
            if start == previous:
                result += f"{start}, "
            else:
                result += f"{start}-{previous}, "
            start = num
            previous = num
        else:
            previous = num
    if start is not None:
        if start == previous:
            result += f"{start}, "
        else:
            result += f"{start}-{previous}"
    print(result.strip(", "))
main()
