EvenNum = lambda No : (No % 2 == 0) if True else False

def main():

    print("Enter the number : ")
    No = int(input())

    iRet = EvenNum(No)

    if(iRet == True):

        print("The Number is Even")

    else:

        print("The number is not a even number")


if __name__ == "__main__":
    main()