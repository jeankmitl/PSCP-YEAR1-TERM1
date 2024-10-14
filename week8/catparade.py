'''catparade'''
def main():
    'bbryg'
    cats = []
    #the funny loop
    while True:
        cat = input()
        if cat == 'END':
            break
        if ',' in cat:
            cat = cat.split(', ')
        if "IT'S A DOG" in cat:
            #when the text "it's a dog" appears, it removes the previous item in the 'cats' list
            if isinstance(cat, list):
                pos = cat.index("IT'S A DOG")
                cat.pop(pos-1)
                cat.pop(pos)
                pos = 0
                cats.extend(cat)
            else:
                cats.pop(-1)
                cat = None
        if isinstance(cat, str) and "IT'S A DOG" not in cat:
            #i dont think the and part is necessary but oh well lol
            cats.append(cat)
        elif isinstance(cat, list):
            cats.extend(cat)

    previous = "lol"
    for i in sorted(cats):
        #this sorts the list out alphabetically
        if i == previous:
            pass
        else:
            count = cats.count(i)
            poss = cats.index(i)
            print(f'{i} {poss+1} {count}')
        previous = i
main()
