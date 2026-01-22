PowerTwo = lambda No : No ** 2

def main():

    iRet = 0

    print("Enter the number : ")
    No = int(input())

    iRet = PowerTwo(No)

    print("The power of two is : ",iRet)


if __name__ == "__main__":
    main()