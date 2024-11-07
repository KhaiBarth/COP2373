# In this program, I am creating a class that displays bank account info. The program takes interest rate, the amount of days and displays the changes these two inputs have depending on their value.



class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        """Adjust the interest rate of the account."""
        self.interest_rate = new_rate
        print(f"Interest rate updated to {self.interest_rate}%.")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount}. New balance: ${self.amount}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and self.amount >= amount:
            self.amount -= amount
            print(f"Withdrew ${amount}. New balance: ${self.amount}.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient funds for withdrawal.")

    def calculate_interest(self, days):
        """Calculate interest based on the number of days."""
        interest = (self.amount * (self.interest_rate / 100) * days) / 365
        return interest

    def balance(self):
        """Return the current balance."""
        return self.amount

    def __str__(self):
        """Return a string representation of the account's current balance and interest rate."""
        return (f"Account holder: {self.name}\n"
                f"Account number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate}%")


# Create test to show functionality
def test_bank_account():
    # Create a BankAcct
    account = BankAcct("Khai Bartholomew", "218793511519", 19000.0, 5.0)

    # Print account details
    print(account)

    # Test deposit
    account.deposit(1000)

    # Test withdrawal
    account.withdraw(500)

    # Test interest rate
    account.adjust_interest_rate(3.0)

    # Calculate interest for a set amount of days
    interest = account.calculate_interest(90)
    print(f"Interest for 90 days: ${interest:.2f}")

    # Print final account details
    print(account)



if __name__ == "__main__":
    test_bank_account()
