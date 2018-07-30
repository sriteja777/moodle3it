O = object

class X(O): pass
class Y(O): pass
class Z(O): pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass
print "mro=", M.mro()
class M(A,B,Z): pass
print "mro=", M.mro()


# Error: cross reference
class A(O): pass 
class B(O): pass 
class Y(B,A): pass
class X(A,B): pass
class Z(X,Y):pass
print(Z.mro()) #Error


