'''CuteCat CuteFox'''
def parse_line(line):
    line = line.strip().replace('{', '').replace('}', '').replace('"', '').replace(' ', '')
    key, value = line.split(':')

    return {key: value}

def main():
    'catgirls or fox girls'
    num = int(input())

    #adds to a seperate dictionary for cats and foxes
    foxes = {}
    cats = {}
    for _ in range(num):
        creature = parse_line(input())
        for name, animal in creature.items():
            if 'Fox' in animal:
                foxes[name] = animal
            elif 'Cat' in animal:
                cats[name] = animal

    #checks for missing creature at 01 index (this took me a while to solve)
    if 'Cat01' not in cats.values() and 'Garfield' not in cats:
        if 'Garfield' not in foxes:
            cats["Garfield"] = "Cat01"

    if 'Fox01' not in foxes.values() and 'Fubuki' not in foxes:
        if 'Fubuki' not in cats:
            foxes["Fubuki"] = "Fox01"

    #sort by items
    if cats:
        cats = dict(sorted(cats.items(), key=lambda item: item[1]))
    if foxes:
        foxes = dict(sorted(foxes.items(), key=lambda item: item[1]))

    #count
    cats_amount = len(cats)
    foxes_amount = len(foxes)

    #print
    print(f"Cat : {cats_amount}")
    print(f"Fox : {foxes_amount}")
    for i, ij in cats.items():
        print(f"{i} : {ij}")
    for j, jj in foxes.items():
        print(f"{j} : {jj}")
main()
