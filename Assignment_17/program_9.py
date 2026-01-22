def CountDigits(No):

    iCount = 0

    while (No != 0):

        No = No // 10
        iCount = iCount + 1

    return iCount     


def main():

    iRet = 0

    print("Enter the Digit : ")
    No = int(input())

    iRet = CountDigits(No)

    print("The number of digits are : ",iRet)


if __name__ == "__main__":
    main()