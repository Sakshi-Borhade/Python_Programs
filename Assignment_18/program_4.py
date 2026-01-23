def Frequency(Data, No):

    iCnt = 0

    for value in Data:

        if(value == No):

            iCnt = iCnt + 1

    return iCnt


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

    print("Enter the value to check : ")
    No = int(input())

    iRet = Frequency(Data,No)
    print("The frequency of that number is : ",iRet)


if __name__ == "__main__":
    main()