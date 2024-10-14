'''rightarrow'''
import math
def arrow():
    '''slide to the right, criss cross!'''
    width = int(input())
    height = int(input())
    space = " "
    star = "*"
    top = math.floor(height // 2)
    bottom = math.ceil(height / 2)
    for i in range(top):
        print((space * i) + (star * width))
    for j in reversed(range(bottom)):
        print((space * j) + (star * width))
arrow()
