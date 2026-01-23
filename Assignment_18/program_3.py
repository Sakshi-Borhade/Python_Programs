def Minimum(No):

    iMin = No[0]

    for value in No:

        if(value < iMin):

            iMin = value

    return iMin


def main():

    Data = []
    iRet = 0

    print("Enter the number of elements that you want to enter : ")
    size = int(input())

    print("Enter the numbers : ")
    for i in range(size):

        Result = int(input())

        Data.append(Result)

    print("The elements are : ",Data)

    iRet = Minimum(Data)
    print("Minimum is : ",iRet)


if __name__ == "__main__":
    main()