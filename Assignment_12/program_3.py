def Calculator(No1, No2):

    Ans1 = 0
    Ans1 = No1 + No2
    
    Ans2 = 0
    Ans2 = No1 - No2

    Ans3 = 0
    Ans3 = No1 * No2

    Ans4 = 0
    Ans4 = No1 / No2

    return Ans1,Ans2,Ans3,Ans4

def main():

    iRet1 = 0
    iRet2 = 0
    iRet3 = 0
    iRet4 = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    iRet1,iRet2,iRet3,iRet4 = Calculator(No1, No2)

    print("Addition is : ",iRet1)
    print("Subtraction is : ",iRet2)
    print("Multiplication is : ",iRet3)
    print("Division is : ",iRet4)


if __name__ == "__main__":
    main()