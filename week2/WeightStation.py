"i love weightstaion :D"
average_weight3 = float(input())
weight1 = float(input())
weight2 = float(input())
weight3 = float(input())
weight4 = (average_weight3 * 4) - (weight1 + weight2 + weight3)
total =  weight1 + weight2 + weight3 + weight4
average_weight4 = total // 4
def overweight(x):
    "checks if it's overweight"
    if x > 15000:
        print("Overweight")
        return False
    return True
def unbalance(avg, w, x, y, z):
    "unbalance"
    increment = (avg // 2) + avg
    if x >= increment or x <= (increment - avg):
        print("Unbalance")
        return False
    if y >= increment or y <= (increment - avg):
        print("Unbalance")
        return False
    if z >= increment or z <= (increment - avg):
        print("Unbalance")
        return False
    if w >= increment or w <= (increment - avg):
        print("Unbalance")
        return False
    return True
if overweight(total) :
    if unbalance(average_weight4, weight1, weight2, weight3, weight4):
        print(f"Pass {weight4:.2f}")
