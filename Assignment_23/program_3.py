class Numbers:

    def __init__(self,A):

        self.Value = A


    def ChkPrime(self):

        for i in range(2, int(self.Value ** 0.5) + 1):
            if (self.Value % i == 0):
                return False

        return True
    
    def Perfect(self):
        
        self.total = 0
        for i in range(1, self.Value):
            if (self.Value % i == 0):
                self.total += i

        return self.total == self.Value
    
    def Factors(self):

        print(f"Factors of {self.Value} are :", end=" ")

        for i in range(1, self.Value + 1):
            if (self.Value % i == 0):
                print(i, end=" ")

    def SumFactors(self):

        self.total = 0
        for i in range(1, self.Value + 1):
            if (self.Value % i == 0):
                self.total += i

        return self.total
    

def main():

    No1 = int(input("Enter the number to check : "))

    obj1 = Numbers(No1)

    Ret = obj1.ChkPrime()
    if(Ret == True):

        print("The number is prime number")

    else:

        print("The number is not a prime number")

    Ret = obj1.Perfect()
    if(Ret == True):

        print("The number is a perfect number")

    else:

        print("The number is not a perfect number")

    obj1.Factors()

    print()

    print("The summation of the factors are : ",obj1.SumFactors())


if __name__ == "__main__":
    main()