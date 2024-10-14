'''frame'''
def main():
    '''big ghyatt frame'''
    star = "*"
    space = ' '
    aa = input().rstrip()
    bb = input().rstrip()
    cc = input().rstrip()
    dd = input().rstrip()
    ee = input().rstrip()
    wordlis = [aa, bb, cc, dd, ee]
    length_word = [len(aa), len(bb), len(cc), len(dd), len(ee)]
    longest_num = max([len(aa), len(bb), len(cc), len(dd), len(ee)])
    print(f'{star*2}{star * (longest_num)}{star*2}')
    for j in range(5):
        print(f'{star + space}{wordlis[j]}{space * (longest_num - length_word[j])}{space + star}')
    print(f'{star*2}{star * (longest_num)}{star*2}')
main()
