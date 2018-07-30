a=0
def foo():
    a=1
    def bar():
        a=2 
        def baz():
            a=3
            print "inside baz:",a
        baz()
        print "inside bar:",a
    bar()
    print "inside foo:",a
foo()
print "outside foo:",a
#################################################
def foo():
    "An example to create calling env. different from creation time env for function baz." 
    a=1
    def bar():
        "bar returns a function baz"
        a=2 
        def baz():
            "baz simply returns a as it sees"
            print "inside baz: a = ",a
            return a
        return baz
    a = 10    
    print foo.__doc__
    print "inside foo: a = ",a
    print bar.__doc__
    f = bar()
    print f.__doc__
    f()
foo()
    

