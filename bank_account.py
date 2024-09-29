# Enhanced Bank Account Management System with Loan Feature

# Initialize lists to hold account data
account_holders = []  # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = []  # List to store outstanding loans for each account

MAX_LOAN_AMOUNT = 10000  # Maximum loan amount
INTEREST_RATE = 0.03  # Interest rate for loans


def create_account():
    """Create a new bank account."""
    # 1. Prompt the user for the account holder's name.
    new_account = input("Create new account. Enter your name: ")
    # 2. Add the new account holder to the list of account holders.
    account_holders.append(new_account)
    # 3. Initialize the balance to 0 for the new account.
    balances.append(0)
    # 4. Initialize an empty transaction history for the new account.
    transaction_histories.append([])
    # 5. Initialize the outstanding loan amount to 0.
    loans.append(0)
    # 6. Notify the user of the successful account creation.
    print(f"Account created for {new_account}.")


def deposit():
    """Deposit money into an account."""
    # 1. Prompt the user for the account holder's name.
    account_name = input("Enter your name: ")
    # 2. Check if the account exists in the system.
    if account_name in account_holders:
        # 3. If the account exists, prompt the user for the amount to deposit.
        amount_to_deposit = float(input('Enter the amount to deposit: '))
        # 4. Update the account's balance with the deposited amount.
        balances[account_holders.index(account_name)] += amount_to_deposit
        # 5. Log the transaction in the account's transaction history.
        transaction_histories[account_holders.index(account_name)].append(f"Deposited: ${amount_to_deposit:.2f}")
        # 6. Display the updated balance to the user.
        print(f"Deposit successful. Updated balance: ${balances[account_holders.index(account_name)]:.2f}")
    # 7. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def withdraw():
    """Withdraw money from an account."""
    # 1. Prompt the user for the account holder's name.
    account_name = input("Enter your name: ")
    # 1. Prompt the user for the account holder's name.
    # 2. Check if the account exists in the system.
    if account_name in account_holders:
        # 3. If the account exists, prompt the user for the amount to withdraw.
        amount_to_withdraw = float(input('Enter the amount to withdraw: '))
        # 4. Check if there are sufficient funds for the withdrawal.
        if balances[account_holders.index(account_name)] >= amount_to_withdraw:
            # 5. If funds are sufficient, update the balance and log the transaction.
            balances[account_holders.index(account_name)] -= amount_to_withdraw
            transaction_histories[account_holders.index(account_name)].append(f"Withdrew: ${amount_to_withdraw:.2f}")
            # 6. Display the updated balance to the user.
            print(f"Withdrawal successful. Updated balance: ${balances[account_holders.index(account_name)]:.2f}")
        # 7. If insufficient funds, inform the user.
        else:
            print("Insufficient funds.")

    # 8. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def check_balance():
    """Check the balance of an account."""
    # 1. Prompt the user for the account holder's name.
    account_name = input("Enter your name: ")
    # 2. Check if the account exists in the system.
    if account_name in account_holders:
        # 3. If the account exists, display the current balance.
        print(f"Current balance: ${balances[account_holders.index(account_name)]:.2f}")
    # 4. If the account does not exist, inform the user.
    else:
        print("Account not found.")


def list_accounts():
    """List all accounts and their balances."""
    # 1. Check if there are any accounts in the system.
    if account_holders:
        # 2. If there are accounts, loop through each account holder.
        print("Account Holders:")
        for i, account_holder in enumerate(account_holders):
            # 3. Display the account holder's name, balance, and outstanding loan amount.
            print(f"{i+1}. {account_holder}: ${balances[i]:.2f}")
    # 4. If there are no accounts, inform the user.
    else:
        print("No accounts found.")


def transfer_funds():
    """Transfer funds between two accounts."""
    # 1. Prompt the user for the sender's and recipient's account holder names.
    sender_name = input("Sender's Name: ")
    recipient_name = input("Recipient's Name: ")
    # 2. Check if both accounts exist in the system.
    if sender_name in account_holders and recipient_name in account_holders:
        # 3. If both accounts exist, prompt the user for the amount to transfer.
        amount_to_transfer = float(input('Enter amount to transfer: '))
        # 4. Check if the sender has sufficient funds for the transfer.
        if balances[account_holders.index(sender_name)] >= amount_to_transfer:
            # 5. If funds are sufficient, update both balances and log the transactions.
            balances[account_holders.index(sender_name)] -= amount_to_transfer
            balances[account_holders.index(recipient_name)] += amount_to_transfer
            transaction_histories[account_holders.index(sender_name)].append(
                f"Transferred to {recipient_name}: ${amount_to_transfer:.2f}")
            transaction_histories[account_holders.index(recipient_name)].append(
                f"Received from {sender_name}: ${amount_to_transfer:.2f}")
            # 6. Inform the user of the successful transfer.
            print('Transfer was successful.')
        # 7. If insufficient funds or if either account does not exist, inform the user.
        else:
            print('Insufficient funds.')

    else:
        print('Either of the accounts does not exist.')


def view_transaction_history():
    """View transaction history for a specific account."""
    # 1. Prompt the user for the account holder's name.
    account_name = input("Enter your name: ")

    # 2. Check if the account exists in the system.
    if account_name in account_holders:
        # 3. If the account exists, display the transaction history.
        print(f"Transaction History for {account_name}:")
        for transaction in transaction_histories[account_holders.index(account_name)]:
            print(transaction)
            # 4. If there are no transactions, inform the user.
        else:
            print("No transactions found.")
    else:
        # 5. If the account does not exist, inform the user.
        print("Account not found.")


def apply_for_loan():
    """Apply for a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for the loan amount they wish to apply for
        loan_amount = float(input(f"Enter the loan amount (max {MAX_LOAN_AMOUNT} leva): "))

        # Check if the loan amount is within the limit
        if loan_amount <= MAX_LOAN_AMOUNT:
            # Update balance and loan amount
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + INTEREST_RATE)  # Calculate total loan with interest

            print(f"Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.")
        else:
            print(f"Loan amount exceeds maximum limit of {MAX_LOAN_AMOUNT} leva.")
    else:
        print("Account not found.")


def repay_loan():
    """Repay a loan."""
    name = input("Enter the account holder's name: ")

    # Check if the account exists in the system
    if name in account_holders:
        index = account_holders.index(name)  # Find the account index

        # Prompt user for repayment amount
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {loans[index]:.2f} leva): "))

        # Check if the repayment amount is valid
        if repayment_amount <= loans[index]:
            # Update balance and outstanding loan amount
            balances[index] -= repayment_amount
            loans[index] -= repayment_amount

            print(
                f"Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan: {loans[index]:.2f} leva.")
        else:
            print("Repayment amount exceeds outstanding loan.")
    else:
        print("Account not found.")


def display_menu():
    """Display the main menu."""
    print('\n--------------------------------------')
    print("--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")
    print('--------------------------------------')

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")


main()
