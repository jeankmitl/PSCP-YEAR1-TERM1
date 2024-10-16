def main():
    '''this is not so peak'''
    sounds = ['ka', 'ba', 'ta']
    words = int(input())

    results = []
    for _ in range(words):
        word = input()
        status = 'yes'
        i = 0
        while i < len(word):

            if i + 1 < len(word) and word[i:i+2] in sounds:
                i += 2
            else:
                if word[i:i+1] in [s[0] for s in sounds]:
                    i += 1
                else:
                    status = 'no'
                    break

        if status == 'yes' and i < len(word):
            status = 'no'
        results.append(status)

    for result in results:
        print(result)

main()
