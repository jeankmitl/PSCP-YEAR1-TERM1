'''point sorting'''
def sort_pairs(pairs):
    '''aaa'''
    return sorted(pairs, key=lambda pair: (int(pair[0]) + int(pair[1]), -int(pair[1])))
def main():
    '''aaa'''
    output = []
    datasets = int(input())
    for _ in range(1, datasets+1):
        templist = []
        amount = int(input())
        for _ in range(amount):
            coords = input()
            meow = coords.split()
            templist.append(meow)
        output.extend(sort_pairs(templist))
    for i in output:
        print(' '.join(i))
main()
