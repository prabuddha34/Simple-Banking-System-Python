# BANKING PROGRAM
# 1) Deposit
# 2) Withdraw
# 3) Check Balance
# 4) EXIT

balance = 100

def show_balance():
    print("*************************")
    print(f"Your Balance is: $ {balance}")
    print("*************************")

def deposit():
    global balance
    depo = int(input("Enter the money you want to deposit: $"))
    if depo > 0:
        balance += depo
        print(f"${depo} deposited successfully.")
    else:
        print("Invalid deposit amount!")

def withdraw():
    global balance
    withd = int(input("Enter the money you want to withdraw: $"))
    if withd > balance:
        print("Insufficient Balance!")
    elif withd <= 0:
        print("Invalid withdrawal amount!")
    else:
        balance -= withd
        print(f"${withd} withdrawn successfully.")

def show_system():
    print("\n====== BANKING MENU ======")
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Check Balance")
    print("4) Exit")
    print("==========================")

while True:
    show_system()
    try:
        user = int(input("Enter your choice (1,2,3,4): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user == 1:
        deposit()
    elif user == 2:
        withdraw()
    elif user == 3:
        show_balance()
    elif user == 4:
        print("Thanks for using the system. Goodbye!")
        break
    else:
        print("Invalid input! Please try again.")
