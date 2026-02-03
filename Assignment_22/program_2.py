class circle:

    PI = 3.14

    def __init__(self):

        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,Rad):

        self.Radius = Rad

    def CalculateArea(self):

        self.Area = circle.PI * self.Radius * self.Radius
    
    def CalculateCircumference(self):

        self.Circumference = 2 * circle.PI * self.Radius

    def Display(self):

        print("The Radius of Circle is : ",self.Radius)
        print("The area of the circle is : ",self.Area)
        print("The Circumference of the circle is : ",self.Circumference)


def main():

    print("Enter the Radius of the circle : ")
    Rad = int(input())

    obj1 = circle()

    obj1.Accept(Rad)
    obj1.CalculateArea()
    obj1.CalculateCircumference()

    obj1.Display()


if __name__ == "__main__":
    main()