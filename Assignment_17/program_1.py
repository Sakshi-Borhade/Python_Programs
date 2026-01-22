import Arithematic

def main():

    iRet = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    iRet = Arithematic.Add(No1, No2)
    print("Addition is : ",iRet)

    iRet = Arithematic.Subtraction(No1, No2)
    print("Subtraction is : ",iRet)

    iRet = Arithematic.Multiplication(No1, No2)
    print("Multiplication is : ",iRet)

    iRet = Arithematic.Division(No1, No2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()