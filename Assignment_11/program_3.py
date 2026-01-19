def SumDigits(No):

    iSum = 0

    while(No != 0):

        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = SumDigits(No)

    print("The Sum of digits is : ",iRet)



if __name__ == "__main__":
    main()