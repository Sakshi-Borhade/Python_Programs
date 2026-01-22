def ChkPrime(No):

    for i in range(2,No):

        if(No % i == 0):

            return False

    return True    


def main():

    iRet = False

    print("Enter the number : ")
    No = int(input())

    iRet = ChkPrime(No)

    if(iRet == True):

        print("The number is prime")

    else:

        print("The number is not a prime")

if __name__ == "__main__":
    main()