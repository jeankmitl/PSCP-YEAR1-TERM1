'''gradethemdrugs'''
def main():
    '''lol'''
    start = int(input())
    stop = int(input())
    print("pass :", end=" ")
    total = 0
    count = 1
    if start > stop:
        count = -1
        stop -= 1
    else:
        stop += 1
    for i in range(start, stop, count):
        if not i % 2:
            print(i, end=" ")
            total = total + i
    print("")
    print(f"Sum : {total}")
main()
