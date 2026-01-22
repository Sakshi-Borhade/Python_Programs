import threading

EvenSum = 0
OddSum = 0

def SumEvenList(Numbers):

    global EvenSum

    print("Inside SumEvenFact : ",threading.get_ident())

    iSum = 0

    for No in Numbers:

        if(No % 2 == 0):

            iSum = iSum + No

    EvenSum = iSum
    print("The sum of even number in the list is : ",EvenSum)

def SumOddList(Numbers):

    global OddSum

    print("Inside SumOddFact : ",threading.get_ident())

    iSum = 0

    for No in Numbers:

        if(No % 2 != 0):

            iSum = iSum + No

    OddSum = iSum
    print("The sum of odd number in the list is : ",OddSum)

def main():

    Data = [10,11,20,21,30,31]

    t1 = threading.Thread(target = SumEvenList, args = (Data,))
    t1.start()

    t2 = threading.Thread(target = SumOddList, args = (Data,))
    t2.start()

    t1.join()
    t2.join()

    print("End of main")


if __name__ == "__main__":
    main()