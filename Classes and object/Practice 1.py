class Dog(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.li = [3,2,1]

    def speak(self,speak):
        print(speak,"Hi I am", self.name, "and I am ", self.age, "years old")

    def weight(self,weight):
        print("My weigth is ",weight,"kg")

    def food(self,food):
        print("I like to eat",food)

    def pet(self,category="Domestic"):
        print("I am", category,"animal")



tim = Dog("Tim",4)
tim.speak("woof!")
tim.weight(35)
tim.food("Pedigree")
tim.pet()

tim.name()



    
