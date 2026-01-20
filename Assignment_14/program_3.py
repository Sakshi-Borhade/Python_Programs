MaximumNum = lambda No1, No2 : No1 if (No1 > No2) else No2

def main():

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    iRet = MaximumNum(No1, No2)

    print("The Maximum of the two number is : ",iRet)


if __name__ == "__main__":
    main()