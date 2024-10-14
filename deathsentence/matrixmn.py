'''matrices'''
def main():
    '''meow'''
    width = int(input())
    height = int(input())
    numbers = []

    for i in range(width * height):
        num = int(input())
        numbers.append(num)

    for i in range(width):
        for j in range(height):
            print(numbers[i * height + j], end=" ")
        print()
main()
