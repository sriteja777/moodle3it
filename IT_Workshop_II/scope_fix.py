ef foo():
    a = 3
    def bar():
        'bar creates local copy of a the moment it assigns to a'
        a = 5
        
    bar()
    print a #3

foo()


def foo():
   'foo creates an empty class and adds all the variables to it ti be modified by bar'
   class DFoo:pass
   DFoo.a = 3
   
   def bar():
      'bar can see DFoo in outer scope and modify its members as side effect'
      DFoo.a = 5
   bar()
   print DFoo.a #5
if __name__ == '__main__':   
   foo()
