def PrintNumber(No):

    for i in range(No,0,-1):

        print(i)
        

def main():

    print("Enter the Number : ")
    No = int(input())

    PrintNumber(No)


if __name__ == "__main__":
    main()