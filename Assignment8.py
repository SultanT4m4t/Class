PIN = 1234
balance = 1000
withdraw_txn = []
deposit_txn = []
txn = []
print("Welcome to M'adiWoSika Bank")


def check_bal():
    print(f"Balance: GHS{balance}")

def Withdraw():
    global balance
    global txn
    global withdraw_txn
    amount = float(input('Enter amount you want to withdraw: '))
    if amount < 0:
        print("Invalid amount")
    elif amount > balance:
        print(f"Withdrawal amount exceeds balance available. Your balance is GHS{balance}")
    else:
        balance = balance - amount
        print(f"You withdrew GHS{amount}. Balance is {balance}")
        withd = "You withdrew GHS{Amount} Balance: GHS{Balance}".format(Amount = amount, Balance= balance)
        withdraw_txn.append(withd)
        txn.append(withd)

def Deposit():
    global balance
    global txn
    global deposit_txn
    amount = float(input('Enter amount you want to deposit: '))
    if amount < 0:
        print('Invalid amount')
    elif amount == 0:
        print('You cannot deposit nothing')
    else:
        balance = balance + amount
        print(f"You deposited GHS{amount}. Balance is {balance}")
        dep = "You deposited GHS{Amount} Balance: GHS{Balance}".format(Amount = amount, Balance= balance)
        deposit_txn.append(dep)
        txn.append(dep)

def Txn():
    counter = 1
    print("Select Transaction history to view")
    txn_type = int(input('1. Deposits 2. Withdrawals 3. All transactions\nEnter: '))

    #View only deposits
    if txn_type == 1:
        txn_range = int(input('View last ??? deposits: '))
        if len(deposit_txn) == 1:
            print(deposit_txn[0])
        elif txn_range == 0:
            print('Cannot view zero deposits')
        else:
            while txn_range > 0 and counter <= len(deposit_txn):
                print(deposit_txn[-(counter)])
                txn_range = txn_range - 1
                counter+=1
            
    elif txn_type == 2:
        txn_range = int(input('View last ??? deposits: '))
        if len(withdraw_txn) == 1:
            print(withdraw_txn[0])
        elif txn_range == 0:
            print('Cannot view zero withdrawals')
        else:
            while txn_range > 0 and counter <= len(withdraw_txn):                
                print(withdraw_txn[-(counter)])
                txn_range = txn_range - 1
                counter+=1
    elif txn_type == 3:
        txn_range = int(input('View last ??? transactions: '))
        if len(txn) == 1:
            print(txn[0])
        elif txn_range == 0:
            print('Cannot view zero transactions')
        else:
            while txn_range > 0 and counter <= len(txn):                
                print(txn[-(counter)])
                txn_range = txn_range - 1
                counter+=1
    else:
        print('Invalid selection')



count = 1
while True:
    valid_pin = int(input('Enter your four digit PIN: '))
    if valid_pin != PIN and count <3:
        print('Wrong PIN. You have',3-count, 'more retries')
        count += 1

    elif valid_pin!= PIN and count >=3:
        print('You have exceeded your amount of retries')
        break

    else:
        while True:
            if valid_pin == PIN:  
                print('1. Check balance\n2. Withdraw money\n3. Deposit money\n4. View transaction history\n5. Exit')
                choice = input('Enter what you want to do: ')
                if choice == '1':
                    check_bal()
                    
                elif choice == '2':
                    Withdraw()

                elif choice == '3':
                    Deposit()

                elif choice == '4':
                    Txn()

                elif choice == '5':
                    print('Come back and bank with us')
                    break

                else:
                    print('Incorrect Choice')

        break
    


    
# while True:
    # if valid_pin == PIN:  
    #     print('1. Check balance\n2. Withdraw money\n3. Deposit money\n4. View transaction history\n5. Exit')
    #     choice = input('Enter what you want to do: ')
    #     if choice == '1':
    #         check_bal()
            
    #     elif choice == '2':
    #         Withdraw()

    #     elif choice == '3':
    #         Deposit()

    #     elif choice == '4':
    #         Txn()

    #     elif choice == '5':
    #         print('Come back and bank with us')
    #         break



    #     else:
    #         print('Incorrect Choice')
        


    
    

