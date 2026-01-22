def SumFactors(No):

    iSum = 0

    for i in range(1,No):

        if(No % i == 0):

            iSum = iSum + i

    return iSum

def main():

    iRet = 0

    print("Enter the number : ")
    No = int(input())

    iRet = SumFactors(No)

    print("Sum of factors is : ",iRet)

if __name__ == "__main__":
    main()