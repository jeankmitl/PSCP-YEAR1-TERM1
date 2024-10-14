'''wordsequence2'''
def main():
    '''docstrings'''
    #transform from first word to final word lol
    first_word = input()
    final_word = input()

    output = ''
    for i in range(len(final_word) + 1):
        output = ''
        output += final_word[:i]
        output += first_word[i:]
        print(output)

    if len(first_word) > len(final_word):
        for j in range(len(final_word), len(output)):
            print(final_word + output[j+1:])
main()
