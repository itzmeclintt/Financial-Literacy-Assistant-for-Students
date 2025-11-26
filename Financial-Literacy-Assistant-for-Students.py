import datetime

balance = 0
expenses = []

def add_allowance():
    global balance
    print("\n=== ADD ALLOWANCE ===")

    while True:
        try:
            amount = float(input("Enter your allowance amount: ₱"))

            if amount < 0:
                print("Amount cannot be negative. Please try again.")
                continue

            balance += amount
            print(f"Allowance added! Current balance: ₱{balance:.2f}")
            break

        except:
            print("Invalid input! Please enter a valid number.")

def add_expense():
    global balance
    
    print("\n=== ADD EXPENSE ===")
    category = input("Enter expense category (food, transport, etc.): ")

    while True:
        try:
            amount = float(input("Enter expense amount: ₱"))

            if amount < 0:
                print("Invalid input! Amount cannot be negative. Please try again.")
                continue

            if amount > balance:
                print("Not enough balance! Please enter a smaller amount.")
                continue

            break

        except:
            print("Invalid input! Please enter a valid number.")

    balance -= amount
    expenses.append({
        "category": category,
        "amount": amount,
        "date": datetime.date.today()
    })

    print(f"Expense added! Remaining balance: ₱{balance:.2f}")

        
def view_summary():
    print("\n===== Expense Summary =====")
    total_spent = sum(e["amount"] for e in expenses)
    print(f"Total spent: ₱{total_spent:.2f}")
    print(f"Remaining balance: ₱{balance:.2f}\n")
    
    print("Expenses by category:")
    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    
    for cat, amt in categories.items():
        print(f" - {cat}: ₱{amt:.2f}")
        
    print("\nAll expenses with dates:")
    from datetime import date
    for e in expenses:
        print(f"{e['date'].strftime('%d-%m-%Y')} - {e['category']}: ₱{e['amount']:.2f}")

def show_tips():
    import random
    tips = [
        "Save at least 10% of your daily allowance.",
        "Avoid impulse buying — think before you spend.",
        "Bring your own snacks instead of buying outside.",
        "Keep a daily record of where your money goes.",
        "Plan your spending every morning.",
        "Learn to prioritize needs over wants when making financial decisions.",
        "Set long-term financial goals, like saving for education, emergencies, or investments.",
        "Always set a monthly budget to keep track of your income and expenses.",
        "Learn basic financial literacy to understand how saving and investing work.",
        "Look for ways to earn extra income, such as part-time jobs or small businesses.",
    ]
    print("\n💡 Financial Tip:", random.choice(tips))

def main():
    print("Welcome to FinWise - Your Financial Literacy Assistant!")
    print("Please make a selection to get started.")
    while True:
        print("\n==== FinWise Menu ====")
        print("1. Add Allowance")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Show Financial Tip")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_allowance()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            show_tips()
        elif choice == '5':
            print("Goodbye! Stay financially wise! 💰")
            break
        else:
            print("Invalid choice. Try again.")

main()