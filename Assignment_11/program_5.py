def PalindromeDigits(No):

    iTemp = No
    iRev = 0

    while(iTemp != 0):

        iDigit = iTemp % 10
        iRev = (iRev * 10) + iDigit
        iTemp = iTemp // 10

    if(iRev == No):

        return True
    
    else: 

        return False


def main():

    iRet = False

    print("Enter the Number : ")
    No = int(input())

    iRet = PalindromeDigits(No)

    if(iRet == True):

        print("The number is Palindrome")

    else:

        print("The number is not a Palindrome")


if __name__ == "__main__":
    main()