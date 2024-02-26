import tkinter as tk
from tkinter import simpledialog, messagebox

class ATMInterface:
    def __init__(self, root, title="Octa Net Bank"):
        self.root = root
        self.root.title(title)
        self.account_number = "9876543210"
        self.pin = "1234"
        self.balance = 1000.0

        # Login screen
        self.login_screen()

    def login_screen(self):
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()

        self.label_account_number = tk.Label(self.login_frame, text="Account Number:")
        self.label_account_number.pack(pady=10)
        self.entry_account_number = tk.Entry(self.login_frame)
        self.entry_account_number.pack(pady=10)

        self.label_pin = tk.Label(self.login_frame, text="PIN:")
        self.label_pin.pack(pady=10)
        self.entry_pin = tk.Entry(self.login_frame, show="*")
        self.entry_pin.pack(pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.verify_login)
        self.login_button.pack(pady=10)

    def verify_login(self):
        entered_account_number = self.entry_account_number.get()
        entered_pin = self.entry_pin.get()

        if entered_account_number == self.account_number and entered_pin == self.pin:
            self.login_frame.destroy()
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid account number or PIN.")

    def main_menu(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.label = tk.Label(self.main_frame, text="Welcome to Octa Net Bank", font=("Helvetica", 40))
        self.label.pack(padx=20, pady=20)

        self.withdraw_button = tk.Button(self.main_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack(pady=10)

        self.transfer_button = tk.Button(self.main_frame, text="Transfer", command=self.transfer)
        self.transfer_button.pack(pady=10)

        self.history_button = tk.Button(self.main_frame, text="Transaction History", command=self.transaction_history)
        self.history_button.pack(pady=10)

        self.deposit_button = tk.Button(self.main_frame, text="Deposit", command=self.deposit)
        self.deposit_button.pack(pady=10)

        self.balance_button = tk.Button(self.main_frame, text="Check Balance", command=self.check_balance)
        self.balance_button.pack(pady=10)

        self.quit_button = tk.Button(self.main_frame, text="Quit", command=self.quit)
        self.quit_button.pack(pady=10)

    def withdraw(self):
        amount = self.get_amount("Enter withdrawal amount:")
        if amount:
            if self.balance >= amount:
                self.balance -= amount
                messagebox.showinfo("Withdrawal", f"Withdrew {amount}$ from your account.")
            else:
                messagebox.showerror("Error", "Insufficient funds.")

    def transfer(self):
        amount = self.get_amount("Enter transfer amount:")
        if amount:
            recipient = self.get_input("Enter recipient's account number:")
            messagebox.showinfo("Transfer", f"Transferred {amount}$ to account {recipient}.")

    def deposit(self):
        amount = self.get_amount("Enter deposit amount:")
        if amount:
            self.balance += amount
            messagebox.showinfo("Deposit", f"Deposited {amount}$ into your account.")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is {self.balance}$.")

    def transaction_history(self):
        messagebox.showinfo("Transaction History", "No transactions yet.")

    def get_amount(self, message):
        amount = simpledialog.askfloat("Amount", message)
        return amount if amount is not None else None

    def get_input(self, message):
        recipient = simpledialog.askstring("Recipient", message)
        return recipient

    def quit(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    app = ATMInterface(root)
    root.geometry("800x600")
    root.mainloop()

if __name__ == "__main__":
    main()
