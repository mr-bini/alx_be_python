import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    parts = sys.argv[1].split(':')

    command = parts[0].lower()

    # Handle deposit and withdraw commands with amount
    if command in ("deposit", "withdraw"):
        if len(parts) != 2:
            print(f"Usage: python main-0.py {command}:<amount>")
            sys.exit(1)

        try:
            amount = float(parts[1])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

        if command == "deposit":
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        elif command == "withdraw":
            if account.withdraw(amount):
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
