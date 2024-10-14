'''gcd???'''
def main():
    '''more like OCD'''
    a = int(input())
    b = int(input())
    while b:
        a, b = b, a % b
    print(a)
main()
