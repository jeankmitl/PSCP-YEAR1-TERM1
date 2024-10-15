'''horizontalhisto'''
def main():
    '''horizontalllll'''
    word = input()

    #coutns, adds dashes and then appends to a list
    letters = {}
    for i in set(word):
        if not word:
            break

        amount = word.count(i)
        outputtemp = ''
        #if count hits 5, add a '|' // if it is a divisor of 5, no need to
        for j in range(1, amount+1):
            outputtemp += '-'
            if not j % 5 and amount - j:
                outputtemp += '|'
        letters[i] = outputtemp

    #sorting
    letters = dict(sorted(letters.items(), key=lambda x: (x[0].isupper(), x[0])))

    #print
    for letter, dashes in letters.items():
        print(f"{letter} : {dashes}")
    #count

main()
