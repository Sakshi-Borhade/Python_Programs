from functools import reduce

EvenNum = lambda No : No % 2 == 0

Square = lambda No : No ** 2

Addition = lambda No1, No2 : No1 + No2

def main():

    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the elements : ")
    for i in range(1,size+1):

        No = int(input())
        Data.append(No)

    print("Entered elements are : ",Data)

    FData = list(filter(EvenNum,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after map is : ",MData)

    RData = reduce(Addition,MData)
    print("Data after reduce is : ",RData)


if __name__ == "__main__":
    main()