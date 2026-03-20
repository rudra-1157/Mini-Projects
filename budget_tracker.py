import json
import os

class BudgetTracker:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        # Default data structure
        self.data = {
            "income": [],
            "expenses": []
        }
        self.load_data()

    def load_data(self):
        """Loads data from the JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading data file. Starting with an empty budget.")

    def save_data(self):
        """Saves current data to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_transaction(self, transaction_type, amount, description):
        """Adds an income or expense record."""
        transaction = {
            "amount": amount,
            "description": description
        }
        self.data[transaction_type].append(transaction)
        self.save_data()
        print(f"\n✅ Successfully added {transaction_type}: ${amount:.2f} for '{description}'.")

    def get_total(self, transaction_type):
        """Calculates the total sum for a specific category."""
        return sum(item["amount"] for item in self.data[transaction_type])

    def view_summary(self):
        """Displays the total income, expenses, and current balance."""
        total_income = self.get_total("income")
        total_expense = self.get_total("expenses")
        balance = total_income - total_expense

        print("\n" + "="*25)
        print("📊 BUDGET SUMMARY")
        print("="*25)
        print(f"Total Income:   +${total_income:.2f}")
        print(f"Total Expenses: -${total_expense:.2f}")
        print("-" * 25)
        
        if balance >= 0:
            print(f"Net Balance:     ${balance:.2f} 🟢")
        else:
            print(f"Net Balance:    -${abs(balance):.2f} 🔴")
        print("="*25)

    def view_history(self):
        """Displays all past transactions."""
        print("\n" + "="*30)
        print("📜 TRANSACTION HISTORY")
        print("="*30)
        
        print("\n--- INCOME ---")
        if not self.data["income"]:
            print("No income recorded.")
        for item in self.data["income"]:
            print(f"  + ${item['amount']:>8.2f} | {item['description']}")

        print("\n--- EXPENSES ---")
        if not self.data["expenses"]:
            print("No expenses recorded.")
        for item in self.data["expenses"]:
            print(f"  - ${item['amount']:>8.2f} | {item['description']}")
        print("="*30)


def main():
    tracker = BudgetTracker()

    while True:
        print("\n" + "*"*30)
        print("💰 PERSONAL BUDGET TRACKER")
        print("*"*30)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget Summary")
        print("4. View Transaction History")
        print("5. Exit")
        print("*"*30)

        choice = input("Enter your choice (1-5): ")

        if choice in ['1', '2']:
            t_type = "income" if choice == '1' else "expenses"
            
            try:
                amount = float(input(f"Enter {t_type} amount: $"))
                if amount <= 0:
                    print("⚠️ Amount must be greater than zero.")
                    continue
                
                description = input("Enter a description (e.g., Salary, Groceries): ")
                tracker.add_transaction(t_type, amount, description)
                
            except ValueError:
                print("⚠️ Invalid input! Please enter a valid number for the amount.")

        elif choice == '3':
            tracker.view_summary()

        elif choice == '4':
            tracker.view_history()

        elif choice == '5':
            print("\nExiting Tracker. Have a great day! 👋\n")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()