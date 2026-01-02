def Addition(No1, No2):
    ans = None
    ans = No1 + No2
    return ans

def Subtraction(No1, No2):
    ans = None
    ans = No1 - No2
    return ans

def Multiplication(No1, No2):
    ans = None
    ans = No1 * No2
    return ans

def Division(No1, No2):
    ans = None
    ans = No1 / No2
    return ans

def Main():
    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    Result = Addition(No1, No2)
    print("Addition is : ",Result)

    Result = Subtraction(No1, No2)
    print("Subtraction is : ",Result)

    Result = Multiplication(No1, No2)
    print("Multiplication is : ",Result)

    Result = Division(No1, No2)
    print("Division is : ",Result)