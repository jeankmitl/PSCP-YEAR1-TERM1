'''parameters'''
def calculate_parity_bit(binar, par):
    '''aaaah'''
    ones = binar.count('1')
    if par == "Even":
        return '1' if ones % 2 != 0 else '0'
    return '0' if ones % 2 != 0 else '1'
def main():
    '''main'''
    binary = input()
    par = input()
    parity_bit = calculate_parity_bit(binary, par)
    result = bin + parity_bit
    print(result)
main()
