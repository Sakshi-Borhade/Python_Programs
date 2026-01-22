from functools import reduce

def PrimeNum(No):

    for i in range(2, No):

        if (No % i == 0):

            return False
        
    return True

Product = lambda No : No * 2

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered elements are : ",Data)

    FData = list(filter(PrimeNum,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Product,FData))
    print("Data after map is : ",MData)

    RData = reduce(Maximum,MData)
    print("Data after reduce is : ",RData)


if __name__ == "__main__":
    main()