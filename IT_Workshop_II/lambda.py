############### lambda - anonymous functions on the fly as needed for a specific purpose as argument to other high order functions ####
a = [1,2,3,4]
b = [17,12,11,10]
print map(lambda x,y:x+y, a,b)

fib = [0,1,1,2,3,5,8,13,21,34,55]
print filter(lambda x: x % 2, fib)
print filter(lambda x: x % 2 == 0, fib)


print reduce(lambda a,b: a if (a > b) else b, [47,11,42,102,13])
print reduce(lambda x,y: x+y, [47,11,42,13])

########### non lambda way - named functions ################
def adder(x,y):
    return x+y
print map(adder, a, b)

