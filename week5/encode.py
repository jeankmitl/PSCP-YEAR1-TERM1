'''encoder'''
def main(code):
    '''encoding sucks tbh'''
    output =''
    count = 1
    letter = code[0]
    for i in code[1:]:
        if i == letter:
            count += 1
        else:
            output += f'{count}{letter}'
            count  = 1
            letter = i
    output += f'{count}{letter}'
    print(output)
main(input())
