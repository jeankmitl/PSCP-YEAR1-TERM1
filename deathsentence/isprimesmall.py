'''prime ENERGY'''
def is_prime(num):
    '''aaa'''
    if num <= 1:
        return "No"
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return 'No'
    return 'Yes'
def main():
    '''main'''
    print(is_prime(int(input())))
main()
