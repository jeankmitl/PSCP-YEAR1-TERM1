'''scndconverter'''
def conv():
    '''this is so stupid i can tfigure the logic of this one liek why'''
    time = int(input("seconds to convert: "))
    second = int(input("second amount of seconds needed to convert: "))
    minute = int(input("minute's amount of seconds needed to convert: "))
    hour = int(input("hours's amount of seconds needed to convert: "))
    secondtrue = time % second
    minutetrue = time // second
    hourtrue = minutetrue // minute
    minutetrue = minutetrue % minute
    hourtrue = hourtrue % hour
    print(f"{hourtrue:d} hours :{minutetrue:d} minutes :{secondtrue:d} seconds")
conv()
