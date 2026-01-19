def ReverseDigits(No):

    iRev = 0

    while(No != 0):

        iDigit = No % 10
        iRev = (iRev * 10) + iDigit
        No = No // 10

    return iRev


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = ReverseDigits(No)

    print("The reverse of digits is : ",iRet)



if __name__ == "__main__":
    main()