'''keeb'''
def meow(stringing):
    '''get a new keyboard pls'''
    sentence = ""
    for char in stringing:
        if char == 'o':
            sentence += 'i'
        elif char == 'O':
            sentence += 'I'
        elif char == 'i':
            sentence += 'o'
        elif char == 'I':
            sentence += 'O'
        else:
            sentence += char
    return sentence
print(meow(str(input())))
