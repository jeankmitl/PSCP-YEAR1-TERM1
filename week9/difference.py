'''difference'''
def setmaker(amount):
    '''aaaa'''
    temp = ''
    for _ in range(amount):
        temp += f'{(input())} '
    temp = temp.rstrip()
    setter = set(int(tem) for tem in temp.split(' '))
    return setter
def main():
    '''THIS IS SO SCUFFED'''
    set_a = int(input())
    set_b = int(input())
    set_a = setmaker(set_a)
    set_b = setmaker(set_b)
    output = sorted(set_a - set_b)
    print(' '.join(map(str, output)))
main()
