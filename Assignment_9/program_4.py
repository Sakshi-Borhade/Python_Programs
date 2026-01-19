def CubeNum(No):

    Ans = 0

    Ans = No ** 3

    return Ans


def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = CubeNum(No)

    print("The Cube of Given Number is : ",iRet)


if __name__ == "__main__":
    main()