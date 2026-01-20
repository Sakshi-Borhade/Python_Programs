def AreaCircle(Radius):

    Pie = 3.14
    Area = 0

    Area = Pie * Radius * Radius

    return Area

def main():

    iRet = 0

    print("Enter the Radius of the Circle : ")
    Rad = int(input())

    iRet = AreaCircle(Rad)

    print("The area of Circle is : ",iRet)


if __name__ == "__main__":
    main()