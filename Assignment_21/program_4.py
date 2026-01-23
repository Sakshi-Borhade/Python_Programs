import threading

def Product(Numbers):

    iMulti = 1

    print("Inside PrimeNum : ",threading.get_ident())

    for No in Numbers:

        iMulti = iMulti * No
    
    print("The Multiplication is : ",iMulti)

def Addition(Numbers):

    iSum = 0

    print("Inside NonPrime : ",threading.get_ident())

    for No in Numbers:

        iSum = iSum + No
    
    print("The Addition is : ",iSum)

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the Elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered numbers are : ",Data)

    t1 = threading.Thread(target = Product, args = (Data,))
    t2 = threading.Thread(target = Addition, args = (Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()