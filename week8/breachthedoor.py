'''breacher'''
def main():
    '''bruh'''
    chars = ['~', '!', '@', '`', '#', '$', '%', '^', '&', '*', "(", ')', '-', '=', '+' \
        '|', '[', ']', ';', ':', '"', "'", ',', '<', '.', '>', '/', '?']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sentence = input()
    for i in chars:
        if i in sentence:
            sentence = sentence.replace(i, '')
    for j in nums:
        if j in sentence:
            sentence = sentence.replace(j, '')
    transd = sentence.split()

    output = ''
    for i in transd:
        if len(i) > 6:
            output += f"{i} "
    print(output.rstrip())
main()
