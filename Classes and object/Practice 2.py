class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.li = [3,2,1]

    def speak(self):
        print("Hi I am", self.name, "and I am ", self.age, "years old")
    
    def talk(self):
        print("Woof")
    
    def weight(self,weight):
        print("My weigth is ",weight,"kg")

    def food(self,food):
        print("I like to eat",food)

    def pet(self,category="domestic"):
        print("I am a",category,"animal")
        
class Cat(Dog):
    def __init__(self,name, age, color):
        super().__init__(name, age)
        self.color = color
        self.name = "Rosy"
        
    def talk(self):
        print("Meow!")
    
tim = Cat("",5,"brown")
tim.talk()
tim.speak()
tim.food("Fish")
tim.pet()

jim = Dog("Jim",6)
jim.talk()
jim.speak()