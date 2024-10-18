'''safe'''
def comparer(iniletter, safeletter):
    'compare ranges in the alphabet'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    firstindex = alphabet.find(iniletter)
    secindex = alphabet.find(safeletter)

    leftturn = (secindex - firstindex) % 26
    rightturn = (firstindex - secindex) % 26

    return min(leftturn, rightturn)

def main():
    'so safe'
    initialword = input()
    safeword = input()
    total_turns = 0

    #tries to find the smallest amount to chaneg the inputword to safeword
    #why :(
    for i in range(len(safeword)):
        if initialword[i] != safeword[i]:
            total_turns += comparer(initialword[i] ,safeword[i])

    print(total_turns)
main()
