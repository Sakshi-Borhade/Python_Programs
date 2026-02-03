class Arihematic:

    def __init__(self):

        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,A,B):

        self.Value1 = A
        self.Value2 = B

    def Addition(self):

        return self.Value1 + self.Value2
    
    def Substraction(self):

        return self.Value1 - self.Value2
    
    def Multiplication(self):

        return self.Value1 * self.Value2
    
    def Division(self):

        try:

            return self.Value1 / self.Value2
        
        except(ZeroDivisionError):

            print("Division by zero is not possible")


def main():

    No1 = int(input("Enter the first number : "))
    No2 = int(input("Enter the second number : "))

    obj1 = Arihematic()

    obj1.Accept(No1,No2)

    print("Addition is : ",obj1.Addition())
    print("Substraction is : ",obj1.Substraction())
    print("Multiplication is : ",obj1.Multiplication())
    print("Division is : ",obj1.Division())


if __name__ == "__main__":
    main()