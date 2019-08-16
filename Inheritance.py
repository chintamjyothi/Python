# Polygon Class

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides

    def inputSides(self):
        self.sides = [None] * self.n
        for i in range(0,self.n):
            self.sides[i] = int(input("Enter the length of side : "))
        # print(self.sides)

# Traingle class inherits from Polygon

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        for i in self.sides:
            a,b,c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1)

    def findArea(self):
        for i in self.sides:
            a = i
        area = a * a
        print('The area of the Square is %0.2f' %area)

if __name__ == "__main__":

    s = Square()    #square
    s.inputSides()
    s.findArea()
    
    t = Triangle()  #Traingle
    t.inputSides()
    t.findArea()
