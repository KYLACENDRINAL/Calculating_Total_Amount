import tkinter as tk
from tkinter import messagebox

class FruitShopApp:
    def __init__(self, master):
        self.master = master
        master.title("Kyla's Fruit Store")
        master.geometry("1000x300")
        master.configure(bg='#FFD1DC')  # Set background color to a light pink

        self.apple_price = 20
        self.orange_price = 25

        # Set the font for the entire application
        self.custom_font = ("Georgia", 15)

        self.create_welcome_tab()

    def create_welcome_tab(self):
        self.welcome_label = tk.Label(self.master, text="Welcome to Kyla's Fruit Store!", bg='#FFD1DC', font=("Georgia", 30))
        self.welcome_label.pack()

        self.next_button = tk.Button(self.master, text="Next", command=self.create_main_tab, bg='#D2691E', fg='white', font=self.custom_font)
        self.next_button.pack()

    def create_main_tab(self):
        # Destroy the widgets from the welcome tab
        self.welcome_label.destroy()
        self.next_button.destroy()

        # Create the main tab
        self.label = tk.Label(self.master, text="Good day! Have some apple and orange. Prices are indicated below", bg='#FFD1DC', font=self.custom_font)  # Set background color to a light pink
        self.label.pack()

        self.price_label = tk.Label(self.master, text=f"Apple price: {self.apple_price} pesos | Orange price: {self.orange_price} pesos", bg='#FFD1DC', fg='#8B4513', font=self.custom_font)  # Set background color to a light pink, text color to brown, and use the custom font
        self.price_label.pack()
        
        self.label = tk.Label(self.master, text="Kindly input the quantity of apples and oranges you wish to purchase and I'll calculate the amount due", bg='#FFD1DC', font=self.custom_font)  # Set background color to a light pink
        self.label.pack()

        self.frame = tk.Frame(self.master, bg='#FFD1DC')  # Set background color to a light pink
        self.frame.pack()

        self.apple_label = tk.Label(self.frame, text="Apples:", bg='#FFD1DC', font=self.custom_font)  # Set background color to a light pink and use the custom font
        self.apple_label.grid(row=0, column=0)

        self.apple_entry = tk.Entry(self.frame)
        self.apple_entry.grid(row=0, column=1)

        self.orange_label = tk.Label(self.frame, text="Oranges:", bg='#FFD1DC', font=self.custom_font)  # Set background color to a light pink and use the custom font
        self.orange_label.grid(row=1, column=0)

        self.orange_entry = tk.Entry(self.frame)
        self.orange_entry.grid(row=1, column=1)

        self.calculate_button = tk.Button(self.master, text="Calculate Total", command=self.calculate_total, bg='#D2691E', fg='white', font=self.custom_font)  # Set background color to brown, text color to white, and use the custom font
        self.calculate_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.confirm_exit, bg='#FF1493', fg='white', font=self.custom_font)  # Set background color to deep pink, text color to white, and use the custom font
        self.exit_button.pack()

    def calculate_total(self):
        try:
            apple_qty = int(self.apple_entry.get())
            orange_qty = int(self.orange_entry.get())
            total_amount = (apple_qty * self.apple_price) + (orange_qty * self.orange_price)

            messagebox.showinfo("Total Amount", f"Total amount to pay: {total_amount} pesos")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid quantities.")
            
        self.create_Thankyou_tab()

    def create_Thankyou_tab(self):
        self.Thankyou_label = tk.Label(self.master, text="Please prepare the exact amount. Happy purchasing :))!", bg='#FFD1DC', font=("Georgia", 16))
        self.Thankyou_label.pack()

    def confirm_exit(self):
        result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
        if result == "yes":
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FruitShopApp(root)
    root.mainloop()
