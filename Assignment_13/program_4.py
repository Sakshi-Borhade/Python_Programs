def BinaryNum(No):

    Binary = ""

    while (No > 0):

        remainder = No % 2
        Binary = str(remainder) + Binary
        No = No // 2

    return Binary
    

def main():

    iRet = 0

    print("Enter the Number : ")
    No = int(input())

    iRet = BinaryNum(No)

    print("The Binary Number is : ",iRet)


if __name__ == "__main__":
    main()