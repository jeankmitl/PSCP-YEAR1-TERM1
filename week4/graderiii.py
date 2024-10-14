'''graderiii'''
import math
def grader():
    '''why cant we manually grade dis 😭'''
    subjects = int(input())
    total = 0
    if subjects <= 0:
        print("0.00")
        return
    for _ in range(subjects):
        x = float(input())
        if x >= 95:
            score = 4.0
        elif x >= 90:
            score = 3.5
        elif x >= 85:
            score = 3.0
        elif x >= 80:
            score = 2.5
        elif x >= 75:
            score = 2.0
        elif x >= 70:
            score = 1.5
        elif x >= 65:
            score = 1.0
        elif x >= 60:
            score = 0.5
        else:
            score = 0.0
        total += score
    final = total / subjects
    final = math.floor(final * 100)/100.0
    print(f"{final:.2f}")
grader()
