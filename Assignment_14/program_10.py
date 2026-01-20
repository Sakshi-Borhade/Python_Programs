MaximumThree = lambda No1, No2, No3 : No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    print("Enter the third number : ")
    No3 = int(input())

    iRet = MaximumThree(No1,No2,No3)

    print("The Maximum number is : ",iRet)


if __name__ == "__main__":
    main()