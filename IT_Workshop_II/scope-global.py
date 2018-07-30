def foo():
    "accessing global variable"
    print "inside foo:" , s

s = "I am a global variable"
foo()

##############################
def foo():
    "accessing local variable"
    s = "I am local variable"
    print "inside foo:", s

s = "I am a global variable"
foo()
print "outside foo:", s

############################
def foo():
    "error: accessing local variable before its definition"
    print s
    s = "I am local variable"  

s = "I am a global variable"
foo()
##################################
def foo():
    "using global explicitly to show your intentions"
    global s
    s = "I am modified global variable"
    print "inside foo:", s

s = "I am a global variable"
foo()
print "outside foo:", s
########################################
def foo():
    "using local variables outside function gives error"
    t = "I am a local variable"
    print "inside foo:", s
    
foo()
print "outside foo:", t
##########################################
def foo(x,y):
    "example using local, global, arguments"
    x, y = -y, -x
    global a
    a = 10
    b = 20
    print "inside foo:", a,b,x,y


x, y = 1,2
a,b = 3,4
foo(x, y)
print "outside foo:",a,b,x,y
