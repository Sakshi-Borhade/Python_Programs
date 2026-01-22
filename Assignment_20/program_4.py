import threading

Capitalcount = 0
Smallcount = 0
Digitcount = 0

def CountCapital(str):

    print("ID of the Capital thread : ",threading.get_ident())
    print("Name of the Capital thread : ",threading.current_thread().name)

    global Capitalcount

    CntCapital = 0

    for char in str:

        if(char >= "A") and (char <= "Z"):

            CntCapital += 1

    Capitalcount = CntCapital
    print("The number of Capital characters is : ",Capitalcount)

def CountSmall(str):

    print("ID of the Small thread : ",threading.get_ident())
    print("Name of the Small thread : ",threading.current_thread().name)

    global Smallcount

    CntSmall = 0

    for char in str:

        if(char >= "a") and (char <= "z"):

            CntSmall += 1

    Smallcount = CntSmall
    print("The number of Small characters is : ",Smallcount)

def CountDigits(str):

    print("ID of the Digit thread : ",threading.get_ident())
    print("Name of the Digit thread : ",threading.current_thread().name)

    global Digitcount

    CntDigit = 0

    for num in str:

        if(num >= "0") and (num <= "9"):

            CntDigit += 1

    Digitcount = CntDigit
    print("The number of Digits characters is : ",Digitcount)

def main():

    print("Enter the string : ")
    str = input()

    t1 = threading.Thread(target = CountCapital, args = (str,))
    t2 = threading.Thread(target = CountSmall, args = (str,))
    t3 = threading.Thread(target = CountDigits, args = (str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()   
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()