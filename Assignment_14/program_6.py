OddNum = lambda No : (No % 2 != 0) if True else False

def main():

    print("Enter the number : ")
    No = int(input())

    iRet = OddNum(No)

    if(iRet == True):

        print("The Number is Odd")

    else:

        print("The number is not a Odd number")


if __name__ == "__main__":
    main()