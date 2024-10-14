'''fourdirections'''
def branch(x):
    '''had to do this cause too many branches'''
    if x == 'L':
        return ' *    '
    if x == 'R':
        return '   *  '
    if x == 'U':
        return '  *   '
    return ' ***  '
def main():
    '''directions'''
    direction = input()
    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''
    for i in range(len(direction)):
        row1 += '  *   '
    for i in direction:
        if i  == 'L':
            row2 += ' *    '
        elif i  == 'R':
            row2 += '   *  '
        elif i  == 'U':
            row2 += ' ***  '
        else: #D
            row2 += '  *   '
    for j in direction:
        if j in ('L', 'R'):
            row3 += '***** '
        else:
            row3 += '* * * '
    for k in direction:
        row4 += branch(k)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row1)
main()
