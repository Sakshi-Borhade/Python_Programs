Addition = lambda No1, No2 : No1 + No2

def main():

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    iRet = Addition(No1,No2)

    print("Addition is : ",iRet)


if __name__ == "__main__":
    main()