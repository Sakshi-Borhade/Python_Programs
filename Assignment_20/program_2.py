import threading

EvenSum = 0
OddSum = 0

def SumEvenFact(No):

    global EvenSum

    print("Inside SumEvenFact : ",threading.get_ident())

    iSum = 0

    for i in range(1,No+1):

        if(No % i == 0) and (i % 2 == 0):

            iSum = iSum + i

    EvenSum = iSum
    print("The sum of even factors is : ",EvenSum)

def SumOddFact(No):

    global OddSum

    print("Inside SumOddFact : ",threading.get_ident())

    iSum = 0

    for i in range(1,No+1):

        if(No % i == 0) and (i % 2 != 0):

            iSum = iSum + i

    OddSum = iSum
    print("The sum of odd factors is : ",OddSum)

def main():

    print("Enter the number : ")
    No = int(input())

    t1 = threading.Thread(target = SumEvenFact, args = (No,))
    t1.start()

    t2 = threading.Thread(target = SumOddFact, args = (No,))
    t2.start()

    t1.join()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()