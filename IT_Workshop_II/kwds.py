def f(a,b,c):
   print a,b,c

f(1,2,3)

def f(a, b=2, c=3):
   print a,b,c

f(1)

# ** in function call here indicates unpacking of the dictionary to match the positional formals
f(1, **{'b':2, 'c':3})
f(1, 2, **{'c':3})
f(1,2,3)

# ** in function definition indicates variable number of arguments packed in a dictionary key=value format
def f (a, **kwds):
   print "a=",a
   for item in kwds:
      print "item=", item, " val=", kwds[item]

f(1, b=2, c=3, d=4, e=5)
f(1, **{'b':2,'c':3,'d':4,'e':5})
