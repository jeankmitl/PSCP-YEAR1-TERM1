'''ON FRORMNWRIOJRWIEDJ'''
def main():
    '''one for all RAGHHHHHH!!!!!!!!!!!!!!'''
    peeps = int(input())
    output = ''
    star = '*'
    line = '-'
    underline = '_'
    for i in range(1, peeps + 1):
        if i == peeps:
            output += input() + underline + str(i)
        elif not i % 2:
            output += input() + line * i
        elif i % 2:
            output += input() + star * i
    print(output)
main()
