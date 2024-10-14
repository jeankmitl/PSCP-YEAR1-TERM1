'''AAAAAAAAAAAAAAAAAAA'''
import math
def eqx(x):
    '''x'''
    total = 2 + (math.log2(x**2) / ((2 * x) * (math.log2(x))))
    return total
def eqy(n, s):
    '''y'''
    total = ((math.sin(math.radians(30))) + math.sqrt(2 * s)) / (eqx(n) + 3)
    return total
def eqz(k):
    '''z'''
    total = ((eqy(k, k))**2) + ((8456*(((eqx(k)))**4)) / (24*k))
    return total
def main():
    '''main'''
    n = float(input())
    s = float(input())
    k = float(input())
    x = eqx(n)
    y = eqy(n, s)
    z = eqz(k)
    print(f'X: {x:.1f}, Y: {y:.1f}, Z: {z:.1f}')
main()
