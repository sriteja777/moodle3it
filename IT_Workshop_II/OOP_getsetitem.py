class Puppy(object):
    def __init__(self, breed):
        self.breed = breed
        self.name = []
        self.color = []

    def __getitem__(self, name):
        if name in self.name:
            return self.color[self.name.index(name)]
        else:
            return None

    def __setitem__(self, name, color):
        self.name.append(name)
        self.color.append(color)

p = Puppy('beagle')
p['Tabby'] = 'cream'
p['Toeffee'] = 'black'
p['Sweetie'] = 'red'


print p.breed, ':Tabby is', p['Tabby']
    
