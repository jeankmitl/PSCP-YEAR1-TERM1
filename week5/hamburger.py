'''bnurgori'''
def burger_maker():
    '''in func name lol'''
    l_burg = int(input())
    r_burg = int(input())
    bread = "|"
    meat = "*"
    print(f"{bread * l_burg}{meat * ((l_burg *2) + (r_burg  * 2))}{r_burg * bread}")
burger_maker()
