class Dog():
    dogs = []
    
    def __init__(self,name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod
    def num_of_dogs(cls):
        a = len(cls.dogs)
        return a        
        
    @staticmethod
    def woof(n):
        for i in range(n):
            print("Woof!")
            
tim = Dog("Tim")
jim = Dog("Jim")
print(tim.num_of_dogs())