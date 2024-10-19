'''verticalhistogram'''
def main():
    '''we going higher'''
    word = input()

    letters = {}
    for i in word:
        total = 0
        total += word.count(i)
        letters.update({i : total})
        word = word.replace(i, "")

    for letter, amount in letters.items():
        print(letter, amount)
main()
