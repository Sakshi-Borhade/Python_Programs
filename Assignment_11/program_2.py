def CountDigits(No):

    iCount = 0

    while(No != 0):

        No = No // 10
        iCount = iCount + 1

    return iCount


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = CountDigits(No)

    print("The count of digits is : ",iRet)



if __name__ == "__main__":
    main()