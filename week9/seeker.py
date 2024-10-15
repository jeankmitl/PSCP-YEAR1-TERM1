'''seeker'''
def main():
    '''seeker'''
    word = input()

    # adds numbers to a pool, stops if the next letter is alphabhet
    # it makes a number, adds to a total
    numbers = 0
    temp = ''
    for i in word:
        if i.isnumeric():
            temp += i
        else:
            if temp:
                numbers += (int(temp))
                temp = ''

    #remainders
    if temp:
        numbers += int(temp)
    print(numbers)
main()
