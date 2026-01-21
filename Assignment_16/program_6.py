def ChkNum(No):

    if(No > 0):

        print("The number is positive number")

    elif(No < 0):

        print("The number is negative number")

    elif(No == 0):

        print("The number is zero")

def main():

    print("Enter the number : ")
    No = int(input())

    iRet = ChkNum(No)


if __name__ == "__main__":
    main()