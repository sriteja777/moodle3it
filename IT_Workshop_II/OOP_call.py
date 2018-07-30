class Puppy(object):
    def __init__(self, breed, name, color):
        self.breed = breed
        self.name = name
        self.color = color

    def __call__(self, mood):
        if mood == 0:
            print "Happy - Bhoo"
        elif mood == 1:
            print "Request - Iyoo"
        elif mood == 2:
            print "Pain - Kquee"
        else:
            print "Neutral - silent"

p = Puppy('beagle', 'tabby', 'brown')

p(0)
p(1)
p(2)
p(3)
        
            
