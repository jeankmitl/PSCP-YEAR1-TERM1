'''dignity is GONE'''
def summer(number):
    '''meow'''
    val = [int(i) for i in number]
    summe = str(sum(val))
    return summe
def dig():
    '''meow'''
    while True:
        num = input()
        if num == "0":
            break
        while len(num) > 1:
            num = summer(num)
        print(num)
dig()
