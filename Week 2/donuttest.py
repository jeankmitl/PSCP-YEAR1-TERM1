'''donut'''
a = int(input()) #price per one
b  = int(input()) #amount needed for extra
c = int(input()) #extra amount
d = int(input()) #needed amount
extra_added = b + c
times_extra = d // (extra_added)
amount_w_extra = (b * times_extra)
cost = 0
piecetotal = 0

if not d % extra_added:
    piecetotal += (b * times_extra) + (c * times_extra)
    cost += (b * times_extra) * a
elif d % extra_added:
    print("lol")

print(cost, piecetotal)



#make sure to return (pricetotal,  donuttotal)
#need to get the needed amount while spending the least[]
#lower than needed?????[]
#more than needed[]
#equal to needed []
#dont need donuts[]
        

