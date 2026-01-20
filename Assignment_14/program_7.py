Divisible = lambda No : (No % 5 == 0) if True else False

def main():

    print("Enter the number : ")
    No = int(input())

    iRet = Divisible(No)

    if(iRet == True):

        print("The Number is divisible by 5")

    else:

        print("The number is not divisible by 5")


if __name__ == "__main__":
    main()