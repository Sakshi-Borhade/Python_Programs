Multiplication = lambda No1, No2 : No1 * No2

def main():

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    iRet = Multiplication(No1,No2)

    print("Multiplication is : ",iRet)


if __name__ == "__main__":
    main()