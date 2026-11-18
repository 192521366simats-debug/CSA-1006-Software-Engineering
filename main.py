import csv
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.csv")
FIELDS = ["date", "category", "description", "amount"]

def ensure_file():
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()

def add_expense():
    category = input("Category (Food/Travel/Books/etc.): ").strip()
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount (₹): "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    row = {"date": datetime.now().strftime("%Y-%m-%d"),
           "category": category, "description": description, "amount": amount}
    ensure_file()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=FIELDS).writerow(row)
    print("Expense saved!")

def view_expenses():
    ensure_file()
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("No expenses recorded yet.")
        return
    print("\n--- Expense History ---")
    for row in rows:
        print(f'{row["date"]} | {row["category"]} | {row["description"]} | ₹{float(row["amount"]):.2f}')

def show_total():
    ensure_file()
    with DATA_FILE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    total = sum(float(row["amount"]) for row in rows)
    print(f"Total spending: ₹{total:.2f}")

def main():
    while True:
        print("\n=== Student Expense Tracker ===")
        print("1. Add expense\n2. View expenses\n3. Show total\n4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
