def DisplayPattern(No):

    for i in range(No):

        for j in range(No):

            print("*",end = "\t")

        print()

def main():

    print("Enter the number : ")
    No = int(input())

    DisplayPattern(No)

if __name__ == "__main__":
    main()