def DisplayGrade(No):

    if(No <= 100) & (No >= 75):

        print("Distinction")

    elif(No < 75) & (No >= 60):

        print("First Class")

    elif(No < 60) & (No >= 50):

        print("Second Class")

    elif(No < 50):

        print("Fail")

def main():

    print("Enter the grade : ")
    No = int(input())

    DisplayGrade(No)


if __name__ == "__main__":
    main()