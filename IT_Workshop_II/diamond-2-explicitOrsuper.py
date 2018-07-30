class BasicActivity (object):
    def run(self):
        print "basic run"

    def jump(self):
        print "basic jump"

class ChickenStyleActivity(BasicActivity):
    def run(self):
        print "run like chicken"

class BunnyStyleActivity(BasicActivity):
    def jump(self):
        print "jump like bunny"
        # either call to super
        #super(BunnyStyleActivity, self).jump()
        # or use explicit call
        BasicActivity.jump(self)

class ExtraordinaryActivity(ChickenStyleActivity,BunnyStyleActivity):
    pass

d = ExtraordinaryActivity()
d.run()
d.jump()
