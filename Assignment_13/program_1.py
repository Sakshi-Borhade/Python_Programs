def AreaRectangle(length, Breadth):

    Area = 0

    Area = length * Breadth

    return Area

def main():

    iRet = 0

    print("Enter the length of the Rectangle : ")
    len = int(input())

    print("Enter the breadth of the rectangle : ")
    breadth = int(input())

    iRet = AreaRectangle(len,breadth)

    print("The area of Rectangle is : ",iRet)


if __name__ == "__main__":
    main()