'''USA!!!USA!!!!'''
def main():
    '''interstate'''
    num = input()
    if not num.isdigit() or int(num) <= 0:
        print('Other')
        return
    num = int(num)
    length = len(str(num))
    angle = ''
    parent_int = ''
    if length <= 2:
        if num % 10 == 5:
            angle = "Vertical Major Interstate"
        elif not num % 10:
            angle = 'Horizontal Major Interstate'
        parent_int = f'I-{num}'
    elif length == 3:
        if not (num // 100) % 2:
            angle = "Even Minor Interstate"
        else:
            angle = 'Odd Minor Interstate'
        parent_int = f'I-{num % 100}'
    if angle:
        print(angle)
        if parent_int[-2:] == '00':
            parent_int = parent_int[:-1]
        print(parent_int)
    else:
        print('Other')
main()
