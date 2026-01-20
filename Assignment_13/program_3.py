def ChkPerfect(No):

    iSum = 0

    for i in range(1,No):

        if(No % i == 0):

            iSum = iSum + i

    if(iSum == No):

        return True
    
    else:

        return False

def main():

    iRet = False

    print("Enter the Number : ")
    No = int(input())

    iRet = ChkPerfect(No)

    if(iRet == True):

        print("The number is a perfect number")

    else:

        print("The number is not a perfect number")


if __name__ == "__main__":
    main()