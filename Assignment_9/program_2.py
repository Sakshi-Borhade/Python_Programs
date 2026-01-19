def ChkGreater(No1 , No2):

    iMax = 0

    if(No1 > No2):
        iMax = No1

    elif(No2 > No1):
        iMax = No2

    return iMax

def main():

    iRet = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    iRet = ChkGreater(No1, No2)

    print("The Greater number is : ",iRet)


if __name__ == "__main__":
    main()