def MultiTable(No):

    for i in range(1,11):

        print(No * i)


def main():

    print("Enter the Number : ")
    No = int(input())

    MultiTable(No)


if __name__ == "__main__":
    main()