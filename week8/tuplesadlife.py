'''I HATE TUPLES DIE'''
def meow():
    '''ERADICATE!'''
    nums = input()
    numtuple = tuple(num for num in nums.split(" "))
    numb = input()
    find = numtuple.count(numb)
    indexed = numtuple.index(numb)
    printer = f"{str(indexed)} "
    if not indexed:
        indexed += 1
    for _ in range(indexed):
        for _ in range(find):
            temp = printer * find
            print(temp.rstrip())
meow()
