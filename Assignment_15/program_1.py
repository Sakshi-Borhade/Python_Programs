SquareNum = lambda No : No ** 2

def main():

    Data = [2,3,4,5,6]
    print("Actual data is : ",Data)

    MData = list(map(SquareNum,Data))
    print("Data after map is : ",MData)


if __name__ == "__main__":
    main()