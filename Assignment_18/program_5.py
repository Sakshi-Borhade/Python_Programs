from MarvellousNum import ChkPrime

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

    iRet = ChkPrime(Data)
    print("Addition of prime numbers is : ",iRet)

if __name__ == "__main__":
    main()