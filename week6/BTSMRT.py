'''bts'''
def gate():
    '''NO MORE CHILDREN!!'''
    date = input()
    age = float(input())
    height = float(input())
    if date == 'Children Day' and height < 140 and age < 14:
        print('FREE')
    elif date == 'Senior Day' and age >= 60:
        print('FREE')
    else:
        if age < 14 and height < 90:
            print('FREE')
        else:
            print('PAY')
gate()
