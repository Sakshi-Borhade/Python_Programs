import threading

iMax = 0
iMin = float('inf')

def Maximum(Numbers):

    global iMax

    print("Inside PrimeNum : ",threading.get_ident())

    for No in Numbers:

        if(No > iMax):

            iMax = No
    
    print("The maximum number is : ",iMax)

def Minimum(Numbers):

    global iMin

    print("Inside NonPrime : ",threading.get_ident())

    for No in Numbers:

        if(No < iMin):

            iMin = No
    
    print("The minimum number is : ",iMin)

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the Elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered numbers are : ",Data)

    t1 = threading.Thread(target = Maximum, args = (Data,))
    t2 = threading.Thread(target = Minimum, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()