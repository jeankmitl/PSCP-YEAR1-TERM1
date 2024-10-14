'''factor'''
def prime(n):
    '''wooof'''
    factor = {}
    han = 2
    while n > 1:
        while n % han == 0:
            if han in factor:
                factor[han] += 1
            else:
                factor[han] = 1
            n //= han
        han += 1
    return factor
def format_factors(fac):
    '''meow'''
    term = []
    for base in sorted(fac.keys()):
        yokgamlang = fac[base]
        if yokgamlang > 1:
            term.append(f"{base}**{yokgamlang}")
        else:
            term.append(f"{base}")
    return " x ".join(term)
def main():
    '''main'''
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    for number in numbers:
        factors = prime(number)
        total = format_factors(factors)
        print(total)
main()
