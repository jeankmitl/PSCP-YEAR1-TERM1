'''breacher'''
def main():
    '''bruh'''
    chars = ['~', '!', '@', '`', '#', '$', '%', '^', '&', '*', "(", ')', '-', '=', '+' \
        '|', '[', ']', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sentence = input()
    for i in chars:
        if i in sentence:
            sentence = sentence.replace(i, '')
    for j in nums:
        if j in sentence:
            sentence = sentence.replace(j, '')
    transd = sentence.split()

    letters = ['a', 'e', 'i', 'o', 'u']
    sortlist = []
    count = 0
    for i in transd:
        for k in letters:
            count += i.count(k)
        if count > 1:
            sortlist.append(i)
        count = 0
    sortlist = sorted(sortlist)
    if sortlist == []:
        print('Nope')
    else:
        for j in sortlist:
            print(j)
main()
