class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.cordinates = (self.x,self.y)
    
    def move(self,x,y):
        self.x += x
        self.y += y
        print( "("+ str(self.x) + ", " + str(self.y) + ")" )
        
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
          
    def __add__(self,p):
        return (self.x + p.x, self.y + p.y)
    
    def __sub__(self,p):
        return (self.x - p.x, self.y - p.y)
    
    def __mul__(self,p):
        return self.x*p.x + self.y*p.y
    
    def __gt__(self,p):
        return self.length() > p.length()
    
    def __ge__(self,p):
        return self.length() >= p.length()
    
    def __lt__(self,p):
        return self.length() < p.length()
    
    def __le__(self,p):
        return self.length() <= p.length()
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
p1 = Point(3,6)
p2 = Point(2,7)
p3 = Point(-1,4)
p4 = Point(0,6)

p5 = p1 + p2
p6 = p4 - p2
p7 = p3 * p1
p8 = p3 >= p2
p9 = p1 > p4
p1.move(2,4)
print(p5,p6,p7)
print(p8, p9)
