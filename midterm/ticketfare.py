'''ticket'''
def ticket():
    '''what the FUCK are these prices'''
    final_station = int(input())
    enter_station = int(input())
    enter_price = int(input())
    past_station = int(input())
    past_price = int(input())
    limit_station = int(input())
    limit_price = int(input())
    enter = int(input())
    leave = int(input())
    total = 0
    i = enter
    if enter == enter_station:
        
    while i <= final_station:
        if i < enter_station:
            print('Error')
            break
