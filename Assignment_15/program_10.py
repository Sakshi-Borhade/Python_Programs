from functools import reduce

EvenNum = lambda No : (No % 2 == 0)

def main():

    Data = [22,34,45,15,6]
    print("Actual data is : ",Data)

    FData = list(filter(EvenNum,Data))
    print("Data after filter and even number is : ",FData)

    print("Count of the even elements is : ",len(FData))


if __name__ == "__main__":
    main()