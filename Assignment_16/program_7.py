def ChkNum(No):

    if(No % 5 == 0):

        return True
    
    else:

        return False

def main():

    iRet = False

    print("Enter the number : ")
    No = int(input())

    iRet = ChkNum(No)

    if(iRet == True):

        print("The number is divisible by 5")

    else:

        print("The number is not divisible by 5")


if __name__ == "__main__":
    main()