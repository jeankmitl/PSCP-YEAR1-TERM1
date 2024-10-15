'''roman'''
def extras(word, tol):
    '''handles extra nums'''
    if "CM" in word:
        tol += 900
        word = word.replace("CM", "")
    if "CD" in word:
        tol += 400
        word = word.replace("CD", "")
    if "XC" in word:
        tol += 90
        word = word.replace("XC", "")
    if "XL" in word:
        tol += 40
        word = word.replace("XL", "")
    if "IX" in word:
        tol += 9
        word = word.replace("IX", "")
    if "IV" in word:
        tol += 4
        word = word.replace("IV", "")
    return (word, tol)


def main():
    '''ROMANS!!!!!!!!'''
    #this literally just tranlsates roman numerals to a number idk what to tell you
    numeral = input()
    total = 0

    numeral, total = extras(numeral, total)
    for i in numeral:
        if i == "M":
            total += 1000
        elif i == "D":
            total += 500
        elif i == "C":
            total += 100
        elif i == "L":
            total += 50
        elif i == "X":
            total += 10
        elif i == "V":
            total += 5
        elif i == "I":
            total += 1

    #print
    print(total)
main()
