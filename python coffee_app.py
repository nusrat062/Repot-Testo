import tkinter as tk
from tkinter import messagebox

class CoffeeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Shop")
        self.geometry("300x300")
        self.selected_coffee = tk.StringVar()
        self.total_price = tk.DoubleVar()
        self.show_welcome_page()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_welcome_page(self):
        self.clear_window()
        tk.Label(self, text="Welcome to the Coffee Machine!", font=("Arial", 14)).pack(pady=40)
        tk.Button(self, text="Start", command=self.show_selection_page).pack()

    def show_selection_page(self):
        self.clear_window()
        tk.Label(self, text="Select Your Coffee", font=("Arial", 14)).pack(pady=10)

        coffees = {
            "Espresso": 2.5,
            "Latte": 3.0,
            "Cappuccino": 3.5,
            "Mocha": 4.0
        }

        for coffee, price in coffees.items():
            tk.Radiobutton(
                self,
                text=f"{coffee} - ${price:.2f}",
                variable=self.selected_coffee,
                value=coffee,
                command=lambda p=price: self.total_price.set(p)
            ).pack(anchor="w")

        tk.Button(self, text="Next", command=self.show_payment_page).pack(pady=10)

    def show_payment_page(self):
        if not self.selected_coffee.get():
            messagebox.showwarning("No Selection", "Please select a coffee first.")
            return

        self.clear_window()
        tk.Label(self, text="Payment Page", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text=f"Selected: {self.selected_coffee.get()}").pack()
        tk.Label(self, text=f"Price: ${self.total_price.get():.2f}").pack(pady=10)
        tk.Button(self, text="Pay", command=self.show_final_page).pack()

    def show_final_page(self):
        self.clear_window()
        tk.Label(self, text="Thank you!", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text=f"Your {self.selected_coffee.get()} is ready ☕").pack(pady=10)
        tk.Button(self, text="Exit", command=self.destroy).pack(pady=10)

if __name__ == "__main__":
    app = CoffeeApp()
    app.mainloop()