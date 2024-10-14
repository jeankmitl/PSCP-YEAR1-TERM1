'''sequecne'''
def main():
    '''meow'''
    size = int(input())
    stack = int(input())
    square = []
    for i in range(size):
        line = ''
        for j in range(size):
            if not j or not i:
                line += '*'
            elif i == j or i == size-1 or j == size-1 or i+j == size-1:
                line += '*'
            else:
                line += ' '
        square.append(line)
    for k in range(size):
        for _ in range(stack):
            print(square[k], end = ' ')
        print()
main()
