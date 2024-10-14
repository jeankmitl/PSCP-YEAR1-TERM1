'''btu'''
def other(x, h, p, rt, f):
    '''ehight'''
    if h > 8:
        x += (h - 8)*1000

    if p > 2:
        x += (p-2)*600

    if rt == 'kitchen':
        x += 4000

    if f == 'facing the sun':
        x += x * 0.10
    elif f == 'shaded':
        x -= x * 0.10
    return x

def continuer(x, areaa):
    '''bruh'''
    if areaa <= 1400:
        x += 23000
    elif areaa <= 1500:
        x += 24000
    elif areaa <= 2000:
        x += 30000
    elif areaa <= 2500:
        x += 34000
    return x

def main():
    '''way too many'''
    area = int(input())
    height = int(input())
    people = int(input())
    roomtype = input()
    faces = input()
    btutotal = 0

    if  area <= 150:
        btutotal += 5000
    elif area <= 250:
        btutotal += 6000
    elif area <= 300:
        btutotal += 7000
    elif area <= 350:
        btutotal += 8000
    elif area <= 400:
        btutotal += 9000
    elif area <= 450:
        btutotal += 10000
    elif area <= 550:
        btutotal += 12000
    elif area <= 700:
        btutotal += 14000
    elif area <= 1000:
        btutotal += 18000
    elif area <= 1200:
        btutotal += 21000
    else:
        btutotal = continuer(btutotal, area)

    btutotal = other(btutotal, height, people, roomtype,faces)
    print(round(btutotal))
main()
