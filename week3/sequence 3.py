"""sequence3"""
def main():
    '''sequence3'''
    num = int(input())
    for meow in range(1, 5):
        for woof in range(num):
            print(meow + woof, end=" ")
        print()
main()
