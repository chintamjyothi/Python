# Area of Square

class Square:
    def inputSide(self):
        self.side = int(input("Enter the lenght of Square : "))
    def findArea(self):
        a = self.side
        area = a * a
        print('The area of the Square is %0.2f' %area)

if __name__ == "__main__":
    s = Square()
    s.inputSide()
    s.findArea()
