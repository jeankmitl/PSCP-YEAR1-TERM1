"""im so sorry"""
def calc(p1, p2, p3):
    """like genuinely sorry"""
    if p1 > p2:
        if p1 > p3:
            longest = p1
            longest2 = p2 if p2 > p3 else p3
            shortest = p2 if p2 < p3 else p3
        else:
            longest = p3
            longest2 = p1
            shortest = p2
    else:
        if p2 > p3:
            longest = p2
            longest2 = p1 if p1 > p3 else p3
            shortest = p1 if p1 < p3 else p3
        else:
            longest = p3
            longest2 = p1
            shortest = p2
    a_squared = shortest ** 2
    b_squared = longest2 ** 2
    c_squared = longest ** 2
    allow = 0.01
    if abs(a_squared + b_squared - c_squared) <=  allow:
        return "Yes"
    return "No"
plank1 = float(input())
plank2 = float(input())
plank3 = float(input())
print(calc(plank1, plank2, plank3))