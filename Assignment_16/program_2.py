def ChkNum(No):

    if(No % 2 == 0):

        return True
    
    else:

        return False

def main():

    iRet = False

    print("Enter the number : ")
    No = int(input())

    iRet = ChkNum(No)

    if(iRet == True):

        print("The number is even")

    else:

        print("The number is odd")


if __name__ == "__main__":
    main()