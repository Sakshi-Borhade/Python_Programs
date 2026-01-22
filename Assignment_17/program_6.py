def Display(No):

    for i in range(1,No+1):

        for j in range(No,0,-1):

            if(i <= j):

                print("*",end = "\t")

        print()


def main():

    print("Enter the number : ")
    No = int(input())

    Display(No)


if __name__ == "__main__":
    main()