def Addition(No):

    sum = 0

    for value in No:

        sum = sum + value

    return sum


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

    iRet = Addition(Data)
    print("Addition is : ",iRet)


if __name__ == "__main__":
    main()