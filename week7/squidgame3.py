'''squid game'''
def main():
    '''meow'''
    i = 0
    result_a  = 0
    result_b = 0
    while i < 10:
        result_a += int(input())
        i += 1
    j = 0
    while j < 10:
        result_b += int(input())
        j += 1
    if result_a < result_b:
        print('A')
    elif result_b < result_a:
        print('B')
    else:
        print('AB')
main()
