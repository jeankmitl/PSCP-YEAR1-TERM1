'''prime ENEGRY WITH MRBEAST BARS'''
def is_prime(num):
    '''aaa'''
    if num <= 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return 0
    return 1
def main():
    '''cancer'''
    count= 0
    value = int(input())
    for i in range(1, value+1):
        count += is_prime(i)
    print(count)
main()
