'''
    Give the user three tries to enter the correct pin code.
    When the user enters the correct pin code ask them what they want to do.
        Withdraw
        Check balance
    If they want to withdraw ask them how much.
    If they have enough money let them withdraw and display their new balance.
    If they don't have enough money show them their current balance and ask them to withdraw within their limits.
    
'''

pin_code = input("Enter your pin:\n")
# Assuming there is a blance of 10000 in the account
balance = 10000

secret_code = 1234

menu = """
1) Transfer Money
2) Check Balnce
3) Withdraaw
4) Request for Statement
"""
if pin_code != "*771#":
    print("Invalid Pin")
else:
    print(menu)

selection = int(input())
if selection == 1:
    account = float(input("Enter receipient account number: "))
    amount = float(input("Enter amount to transfer: "))
    confirm = int(input("Enter your Secret Code to proceed: "))
    if confirm == secret_code:
        print("Tranfer of GhC",amount,"to this account", account, "SUCCESSFUL")
    else:
        print("Try again")

elif selection == 2:
    print("Your balnce is GhC",balance)

elif selection == 3:
    withdraw = float(input("Enter Amount: "))
    print(f"You've withdrawn GhC {withdraw} Current balance is GhC {balance - withdraw}")
    
    
    