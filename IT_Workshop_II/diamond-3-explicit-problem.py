class A(object):
    def m(self):
        print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
        A.m(self)
    
class C(A):
    def m(self):
        print("m of C called")
        A.m(self)
        
class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)

        

print "Explicit: calling B().m ->", B().m()
print "Explicit: calling C().m ->", C().m()

#A is called twice
print "Explicit: calling D().m ->", D().m()


class A(object):
    def m(self):
        print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
        super(B, self).m()
    
class C(A):
    def m(self):
        print("m of C called")
        super(C, self).m()
        
class D(B,C):
    def m(self):
        print("m of D called")
        super(D, self).m()
       
        

print "super(): calling B().m ->", B().m()
print "super(): calling C().m ->", C().m()

#A is called only once
print "super(): calling D().m ->", D().m() 

