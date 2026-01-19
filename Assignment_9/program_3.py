def SquareNum(No):

    Ans = 0

    Ans = No * No

    return Ans


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = SquareNum(No)

    print("The Square of Given Number is : ",iRet)


if __name__ == "__main__":
    main()