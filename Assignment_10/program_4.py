def EvenNum(No):

    for i in range(2,No+1,2):

        print(i)

def main():

    print("Enter the Number : ")
    No = int(input())

    EvenNum(No)


if __name__ == "__main__":
    main()