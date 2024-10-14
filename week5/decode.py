'''decoder'''
def decode():
    '''megafunnydecoder9000'''
    codes = input()
    decoded = ""
    count = 0
    i = 0
    while i < len(codes):
        if codes[i].isdigit():
            count = count * 10 + int(codes[i])
        elif codes[i].isalpha():
            decoded += count * codes[i]
            count  = 0
        i += 1
    print(decoded)
decode()
