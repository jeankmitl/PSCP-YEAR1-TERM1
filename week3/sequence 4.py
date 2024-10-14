'''SEQUENCEVI'''
def main():
    '''sequence4'''
    num = int(input())
    digit = 1
    for _ in range(num):
        for _ in range(num):
            print(digit, end=' ')
            digit += 1
        print()
main()
