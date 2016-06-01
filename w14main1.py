dogname=raw_input('what is your dog name?')
dogsound=raw_input("What is your dog sound?")
class Dog(object):
    def __init__(self,name, sound):
        self.name=name
        self.sound=sound
    def getName(self):
        print 'Your dog name is', self.name
    def talk(self):
        print 'Your dog sound is', "'",self.sound, "'"
mydog=Dog(dogname, dogsound)
mydog.getName()
mydog.talk()