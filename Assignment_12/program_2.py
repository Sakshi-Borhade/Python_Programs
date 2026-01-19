def FactorsNum(No):

    for i in range(1,No+1):

        if(No % i == 0):

            print(i)
        

def main():

    print("Enter the Number : ")
    No = int(input())

    FactorsNum(No)


if __name__ == "__main__":
    main()