class bankAccount :
    fee = 10
    balance = 0
    pin = "0000"
    def __deposit__(object, amount) :
        object.balance +=  amount
        bankAccount.balance = object.balance
    def __getbalance__(object) :
        object.balance = bankAccount.balance
        return object.balance
    def change_pin(object, pin) :
        object.pin = pin
        return pin
class withdraw(bankAccount) :
        def __init__(object, fee):
            object.fee = fee
        def __withdrawal__(object, amount) :
            bankAccount.balance -= amount + object.fee
            print(super().balance)

classobj = bankAccount()

while True :
    print("1. Check Balance")
    print("2. Withdrawal Amount")
    print("3. Deposit Amount")
    print("4. Change pin")
    print("5. Exit")
    choice = int(input("Enter Choice : "))

    if choice == 1 :
        print("Balance = " + str(classobj.__getbalance__()))
    elif choice == 2 :
        print("Fee charged = " + str(classobj.fee))
        amount = int(input("Enter Amount to be withdraw : "))
        if amount < classobj.balance :
            newobj = withdraw(10)
            newobj.__withdrawal__(amount)
            print("Amount Withdraw successfully")
            print("Total balance = " + str(classobj.__getbalance__()))
        else :
            print("Not sufficient fund")
    elif choice == 3 :
        amount = int(input("Enter Amount to be deposit : "))
        classobj.__deposit__(amount)
        print("Amount Diposit successfully")
        print("Total balance = " + str(classobj.__getbalance__()))
    elif choice == 4 :
        oldpin = str(input("Enter old pin : "))
        if oldpin == classobj.pin :
            pin = str(input("Enter New Pin : "))
            print("New Pin = " + str(classobj.change_pin(pin)))
        else :
            print("Invalid pin!!!")
    elif choice == 5 :
        break   
