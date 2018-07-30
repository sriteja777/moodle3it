class Parent(object):
    def __init__(self):
        super(Parent, self).__init__()
        print "parent"
class Left(Parent):
    def __init__(self):
        super(Left, self).__init__()
        print "left"
class Right(Parent):
    def __init__(self):
        #super(Right, self).__init__()
        print "right"
class Child(Left, Right):
    def __init__(self):
        super(Child, self).__init__()
        print "child"

ch = Child()

class Parent(object):
    def __init__(self):
        print "parent"
        super(Parent, self).__init__()
class Left(Parent):
    def __init__(self):
        print "left"
        super(Left, self).__init__()
class Right(Parent):
    def __init__(self):
        print "right"
        super(Right, self).__init__()
class Child(Left, Right):
    def __init__(self):
        print "child"
        super(Child, self).__init__()

#ch = Child()
