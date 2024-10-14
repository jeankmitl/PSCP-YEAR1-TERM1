'''letfreqw'''
def main():
    '''uiahtehtis'''
    sentence = input().lower()
    output = ''
    max_count = 0

    filtered_sentence = ''.join(c for c in sentence if c.isalpha())

    for char in set(filtered_sentence):
        count = filtered_sentence.count(char)
        if count > max_count:
            max_count = count
            output = char

    print(output)
main()
