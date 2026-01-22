from functools import reduce

GreaterNum = lambda No : No if No >= 70 and No <= 90 else None

Increment = lambda No : No + 10

Product = lambda No1, No2 : No1 * No2

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered elements are : ",Data)

    FData = list(filter(GreaterNum,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after map is : ",MData)

    RData = reduce(Product,MData)
    print("Data after reduce is : ",RData)


if __name__ == "__main__":
    main()