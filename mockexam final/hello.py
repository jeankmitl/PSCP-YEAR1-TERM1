'''meow'''
def main():
    '''helloopo'''
    vowels = 'aeiouAEIOU'
    word = input().strip()
    if not any(char in vowels for char in word):
        print(word)
        return
    for i in reversed(word):
        if i in vowels:
            pos = word.rindex(i)
            word = word[:pos] + f'{i*4}' + word[pos+1:]
            break
    print(word)
main()
