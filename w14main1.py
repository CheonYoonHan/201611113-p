dogname=raw_input('what is your dog name?')
class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print 'Your dog name is', self.name
    def talk(self):
        print 'Your dog sound is', "'",self.sound, "'"
class Shihtzu(Dog):
    name=dogname
    sound='si si'
class Maltese(Dog):
    name=dogname
    sound='Mal Mal'

dog1=dogbreed(dogname)
dog1.getName()
dog1.talk()
dog2.getName()
dog2.talk()
