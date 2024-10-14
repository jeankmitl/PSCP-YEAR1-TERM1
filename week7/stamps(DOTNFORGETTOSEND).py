'''stamps'''
def main():
    '''meow'''
    foodamount = int(input())
    a_times = int(input())
    b_stamp = int(input())
    c_use = int(input())
    d_disco = int(input())
    stamps = 0
    total = 0
    for i in range(foodamount):
        i = i*1
        food = int(input())
        while stamps >= c_use and food > 0:
            food -= d_disco
            stamps -= c_use
        if food <= 0:
            food = 0
        if food // a_times:
            stamps += (food // a_times) * b_stamp
        total += food
    print(total)
    print(stamps)
main()
