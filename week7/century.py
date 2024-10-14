'''century'''
def main():
    '''century'''
    amount = int(input())
    meow = []
    for _ in range(amount):
        current_year = input()
        translated = int(current_year[4:])
        century = 0
        if current_year[0:3] in 'B.E.':
            translated -= 543
            century = (translated + 99) // 100
            meow.append(century)
        elif current_year[0:3] in 'A.D.':
            translated += 0
            century = (translated + 99) // 100
            meow.append(century)
        else:
            meow.append('ERROR')
    for i in meow:
        print(i)
main()
