'''socks'''
def main():
    '''meow'''
    unsock = input()
    socks = []
    count = 0
    for i in unsock:
        amount = unsock.count(i)
        pairs = amount//2
        count += pairs
        socks.append(f'{i * 2} ' * pairs)
        unsock = unsock.replace(i, '')
    socks = sorted(socks)
    if not count:
        print('None')
        print(count)
    else:
        print(''.join(socks))
        print(count)
main()
