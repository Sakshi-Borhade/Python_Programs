def ChkDivisible(No):

    if(No % 3 == 0) & (No % 5 == 0):

        return True
    
    else:

        return False


def main():

    iRet = False

    print("Enter the Number : ")
    No = int(input())

    iRet = ChkDivisible(No)

    if(iRet == True):

        print("The Given number is divisible by 3 and 5")
    
    else:

        print("The given number is not divisible by 3 and 5")


if __name__ == "__main__":
    main()