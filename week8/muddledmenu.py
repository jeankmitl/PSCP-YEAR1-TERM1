'''menu'''
def foodpositioner(word, listy):
    '''aaaa'''
    hashtag = word.find('#')
    num = word[hashtag+1:]
    if num == 'N':
        listy.append(word[:hashtag-1])
    elif isinstance(int(num), int):
        listy.insert(int(num)-1, word[:hashtag-1])
    return listy
def main():
    '''bruh'''
    foodlist = []
    nuhuh = []
    while True:
        food = input()
        if food == "DONE":
            break
        if food == "SOMETHING'S WRONG":
            foodlist.clear()
            food = input()
        if food == "CLOSED":
            foodlist.clear()
            break
        if "Can't do:" in food:
            nuhuh.append(food[10:])
        else:
            foodlist = foodpositioner(food, foodlist)
    for nuh in nuhuh:
        if nuh in foodlist:
            foodlist.remove(nuh)
    print(f'Full Course: {foodlist} Reversed: {list(reversed(foodlist))}')
main()
