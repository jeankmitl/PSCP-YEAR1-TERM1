'''neare'''
def main():
    '''location finder'''
    alice = int(input())
    bob = int(input())
    icecream = int(input())
    alice_location = abs(icecream - alice)
    bob_location = abs(icecream - bob)
    if alice_location < bob_location:
        print(f'Alice {alice_location}')
    elif bob_location < alice_location:
        print(f'Bob {bob_location}')
    else:
        print(f'Sundaes {bob_location}')
main()
