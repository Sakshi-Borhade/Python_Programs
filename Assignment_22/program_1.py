class Demo:

    Value = 20

    def __init__(self,A,B):

        self.No1 = A
        self.No2 = B

    def fun(self):

        print("The instance variables by fun are : ",self.No1,self.No2)

    def gun(self):

        print("The instance variables by gun are : ",self.No1,self.No2)


def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()