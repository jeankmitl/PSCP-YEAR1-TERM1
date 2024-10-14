'''fizbuzz'''
def fizzer():
    '''coke or pep'''
    num = int(input())
    counter = 1
    for i in range(counter,num+1):
        if not i%15 :
            print("FizzBuzz")
            counter = counter+1
        elif not i%3 :
            print ("Fizz")
            counter = counter+1
        elif not i%5 :
            print ("Buzz")
            counter = counter+1
        else :
            print(i)
fizzer()
