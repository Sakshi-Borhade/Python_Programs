def Factorial(No):

    iFact = 1

    for i in range(1,No+1):

        iFact = iFact * i
        

    return iFact        


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = Factorial(No)

    print("Factorial is : ",iRet)


if __name__ == "__main__":
    main()