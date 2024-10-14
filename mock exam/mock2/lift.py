'''lift'''
people = int(input())
liftweight = float(input())
TOTALPEEP = 0
TW = 0
OLAG = 0
YOAG = 0
while True:
    if TOTALPEEP == people:
        break
    TOTALPEEP += 1
    age = float(input())
    weight = float(input())
    if age > 12:
        OLAG += 1
    YOAG += 1
    TW += weight
def ageallow(x, y):
    '''IAHETCHIDLREN'''
    if not x and not y:
        return True
    elif y >= 1:
        return True
    return False
def weightallow(w, z):
    '''wah'''
    if z > w:
        return False
    return True
if ageallow(YOAG, OLAG) is True and weightallow(liftweight, TW) is True:
    print("Safe")
else:
    print("Not Safe")
