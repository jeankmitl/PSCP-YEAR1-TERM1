'''filter'''
import json

def main():
    '''noobs'''
    students = json.loads(input())
    passing_score = float(input())

    #sorts out students who has higher or equal score
    passed = {}
    for student, score in students.items():
        if score >= passing_score:
            passed.update({student : score})

    #sorts
    passed = dict(sorted(passed.items()))

    #print
    if not passed:
        print('Nope')
    else:
        for stu, scr in passed.items():
            print(f'{stu}	{scr:.2f}')
main()
