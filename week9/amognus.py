'''amongussssy'''
import json

def main():
    '''main'''
    alive = {}
    #add sussies here
    while True:
        roles = input()
        if roles == 'Start':
            break
        jsoned = json.loads(roles)
        alive.update(jsoned)
    alive = dict(sorted(alive.items()))

    #take em out (death)
    dead = {}
    while True:
        name = input()
        if name ==  'End':
            break
        temp = alive.get(name)
        dead.update({name : temp})
        alive.pop(name)
    dead = dict(sorted(dead.items()))

    #sussy impostors count (yes idk why is it impostOr)
    count = 0
    for peep in alive:
        if alive.get(peep) == 'Impostor':
            count += 1

    print(f'{count} Impostor Remains')
    print('***Alive***')
    for live in alive:
        print(f'{live} : {alive[live]}')
    print('***Dead***')
    for dea, rold in dead.items():
        print(f'{dea} : {rold}')
main()
