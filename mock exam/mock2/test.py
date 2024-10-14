import math

"""AAAAAAAAAAAAAAAAAAAAAA"""
def main(n,s,k):
    """AAAAAAAAAAAAAAAAAAAAAAAAAAAA"""
    x = 2+(math.log(n**2,2)/(2*n)*(math.log(n,2)))
    y = (math.sin(math.radians(30))+math.sqrt(2*s))/((x*n)+3)
    yk = (math.sin(math.radians(30))+math.sqrt(2*k))/((x*k)+3)
    xk = 2+(math.log(k**2,2)/(2*k)*(math.log(k,2)))
    z = (yk**2)+((8456*(xk**4)/(24*k)))
    print(x,y,z)

main(float(input()),float(input()),float(input()))