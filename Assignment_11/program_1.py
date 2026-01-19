def ChkPrime(No):

    for i in range(2, int (No/2) + 1):

        if(No % i == 0):

            return False
        

    return True


def main():

    iRet = False

    print("Enter the Number : ")
    No = int(input())

    iRet = ChkPrime(No)

    if(iRet == True):

        print("The number is a prime number")

    else:

        print("The number is not a prime number")



if __name__ == "__main__":
    main()