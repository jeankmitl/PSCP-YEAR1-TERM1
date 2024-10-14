"""hsitory"""
def cout_letter(string, letter):
    '''aaaaa'''
    total = 0
    for char in string:
        if char == letter:
            total += 1
    return total
def main():
    """emow"""
    intext = str(input()).replace(' ', '')
    word = []
    coutner = []
    for i in intext:
        if i not in coutner:
            number = cout_letter(intext,i)
            word.append(f'{i} = {number}')
            coutner.append(i)
    slot = sorted(word, key=lambda x: (x.lower(), x.isupper()))
    for j in slot:
        print(j)
main()
