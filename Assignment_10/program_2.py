def SumNatural(No):

    iSum = 0

    for i in range(1,No+1):

        iSum = iSum + i

    return iSum


def main():

    print("Enter the Number : ")
    No = int(input())

    iRet = SumNatural(No)

    print("The sum of first N Natural Number is : ",iRet)


if __name__ == "__main__":
    main()