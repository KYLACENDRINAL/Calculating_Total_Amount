import tkinter as tk
from tkinter import ttk, messagebox

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budgeting App")

        # Style Configuration
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#FF69B4")
        self.style.configure("TLabel", background="#FF69B4", font=("Georgia", 16))
        self.style.configure("TButton", background="#FF69B4", font=("Georgia", 16))
        self.style.configure("TNotebook", background="#FF69B4")
        self.style.configure("TNotebook.Tab", background="#FF69B4", font=("Georgia", 16))

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10, expand=True, fill="both")

        # Tab 1: Question
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Question")
        self.label1 = ttk.Label(self.tab1, text="Do you desire apples, uncertain about how many you can purchase within your budget? Fear not, I've got you covered!", wraplength=600)
        self.label1.pack(pady=20)
        self.next_button1 = ttk.Button(self.tab1, text="Next", command=self.show_tab2)
        self.next_button1.pack(pady=10)

        # Tab 2: Enter Money
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Money")
        self.label2 = ttk.Label(self.tab2, text="How much money do you have?:")
        self.label2.pack(pady=20)
        self.money_entry = ttk.Entry(self.tab2)
        self.money_entry.pack(pady=10)
        self.next_button2 = ttk.Button(self.tab2, text="Next", command=self.show_tab3)
        self.next_button2.pack(pady=10)

        # Tab 3: Enter Price
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Price")
        self.label3 = ttk.Label(self.tab3, text="How much does the apple cost?:")
        self.label3.pack(pady=20)
        self.price_entry = ttk.Entry(self.tab3)
        self.price_entry.pack(pady=10)
        self.next_button3 = ttk.Button(self.tab3, text="Next", command=self.show_tab4)
        self.next_button3.pack(pady=10)

       # Tab 4: Calculation
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Calculation")
        self.label4 = ttk.Label(self.tab4, text="Calculation results will be shown here just tap the text below.")
        self.label4.pack(pady=20)
        self.purchase_button = ttk.Button(self.tab4, text="I hope I help you budgeting your money.\nNow purchase some apples, you deserve it!", command=self.calculate_and_show_result)
        self.purchase_button.pack(pady=10)
        # Exit Button
        self.exit_button = ttk.Button(self.tab4, text="Exit", command=self.show_exit_confirmation)
        self.exit_button.pack(pady=10)

    def show_tab2(self):
        self.notebook.select(self.tab2)

    def show_tab3(self):
        self.notebook.select(self.tab3)

    def show_tab4(self):
        self.notebook.select(self.tab4)

    def calculate_and_show_result(self):
        try:
            money = float(self.money_entry.get())
            price = float(self.price_entry.get())
            if money >= price:
                num_apples = money // price
                remaining_money = money % price
                result_text = f"You can buy {int(num_apples)} apples, and you will have {remaining_money:.2f} money remaining."
                self.label4.config(text=result_text)
            else:
                self.label4.config(text="Insufficient funds to purchase apples.")
        except ValueError:
            self.label4.config(text="Please enter valid numerical values for money and price.")

    def show_exit_confirmation(self):
        answer = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if answer == "yes":
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
