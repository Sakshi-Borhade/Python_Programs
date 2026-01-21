def Add(No1, No2):

    Ans = 0

    Ans = No1 + No2

    return Ans

def main():

    iRet = 0

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    iRet = Add(No1,No2)

    print("Addition is : ",iRet)


if __name__ == "__main__":
    main()