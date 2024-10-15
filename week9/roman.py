'''roman'''
def main():
    '''ROMANS!!!!!!!!'''
    #this literally just tranlsates roman numerals to a number idk what to tell you
    numeral = input()
    total = 0

    #conv
    if "CM" in numeral:
        total += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        total += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        total += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        total += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        total += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        total += 4
        numeral = numeral.replace("IV", "")

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
