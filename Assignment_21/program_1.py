import threading

NumPrime = []
NumNonPrime = []

def is_Prime(No):

    for i in range(2,No):

        if(No % i == 0):

            return False
        
    return True

def PrimeNum(Numbers):

    global NumPrime

    print("Inside PrimeNum : ",threading.get_ident())

    for Num in Numbers:

        if(is_Prime(Num)):

            NumPrime.append(Num)
    
    print("The prime numbers are : ",NumPrime)

def NonPrime(Numbers):

    global NumNonPrime

    print("Inside NonPrime : ",threading.get_ident())

    for Num in Numbers:

        if(not(is_Prime(Num))):

            NumNonPrime.append(Num)
    
    print("The non prime numbers are : ",NumNonPrime)

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the Elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered numbers are : ",Data)

    t1 = threading.Thread(target = PrimeNum, args = (Data,))
    t2 = threading.Thread(target = NonPrime, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()