class BankAccount:

    ROI = 10.5

    def __init__(self,A,B):

        self.Name = A
        self.Account = B

    def Display(self):

        print(f"The Account holder {self.Name} contains balance {self.Account}.")

    
    def Deposit(self,Depo):

        self.Account += Depo
        print("Updated Balance after deposit is : ",self.Account)


    def Withdrawal(self,withdraw):

        if(self.Account == 0):

            print("You dont have sufficient Balance to withdraw")
            return

        self.Account -= withdraw
        print("Updated Balance after withdrawal is : ",self.Account)

    def CalculateInterest(self): 

        return (self.Account * BankAccount.ROI) / 100
    

def main():

    obj1 = BankAccount("Sakshi Borhade",30000)
    obj1.Display()
    obj1.Deposit(2000)
    obj1.Withdrawal(2000)
    print("The Rate of interest on the Balance is : ",obj1.CalculateInterest())

if __name__ == "__main__":
    main()