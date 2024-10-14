"i love weightstaion :D"
avg_3w = float(input())
w1 = float(input())
w2 = float(input())
w3 = float(input())
w4 = ((avg_3w*3) - (w1 + w2 + w3))
whattheflip = (avg_3w * 4) / 2
whatthehell = (w1 + w2 + w3 + w4) / 4
def printstupid()
    print(f"Pass {w4:.2f}")
def main():
    ''' i want to kill myself'''
    if  w1 + w2 + w3 + w4 >= 15000:
        print("Overweight")
    else:
        if w1 > avg_3w and w2 > avg_3w and w3 > avg_3w:
            print("Unbalance")
        elif w1 <= avg_3w and w2 <= avg_3w and w3 <= avg_3w and w4 <= avg_3w:
            printstupid()
        elif w1 <= whattheflip and w2 <= whattheflip and w3 <= whattheflip and w4 <= whattheflip:
            printstupid()
        else:
            print("Unbalance")
