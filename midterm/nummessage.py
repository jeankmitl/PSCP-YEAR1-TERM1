'''nuummessageer'''
def main():
    '''aaa'''
    words = input()
    numlis = ['2', '6', '7', '8', '9']
    words = words.replace('12', 'R')
    words = words.replace('13', 'B')
    words = words.replace('1', 'I')
    words = words.replace('3', 'E')
    words = words.replace('4', 'A')
    words = words.replace('5', 'S')
    words = words.replace('0', 'O')
    for i in numlis:
        words = words.replace(i, '')
    words = words.upper()
    print(words)
main()
