def ChkVowel(str):

    if((str == "a") | (str == "e") | (str == "i") | (str == "o") | (str == "u")):

        return True
    
    else:

        False


def main():

    iRet = False

    print("Enter the alphabet : ")
    str = input()

    iRet = ChkVowel(str)

    if(iRet == True):

        print("The alphabet is a vowel")

    else:

        print("The alphabet is not a vowel")


if __name__ == "__main__":
    main()