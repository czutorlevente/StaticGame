import tkinter as tk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.current_frame = None
        self.main_menu()

    def main_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()
        
        tk.Button(self.current_frame, text="Calculate support reactions", command=self.calculate_menu, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=30, )
        tk.Button(self.current_frame, text="Change default units of measurement", command=self.change_menu, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=30)
        tk.Button(self.current_frame, text="Exit", command=self.root.quit, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=50)

    #Calculate menu number 1:
    def calculate_menu(self):
        
        def get_numbers():
            try:
                point_loads = int(entry1.get())
                distributed_loads = int(entry2.get())

                # Check if the input is valid
                if point_loads >= 0 and distributed_loads >= 0:
                    return True, point_loads, distributed_loads
                else:
                    return False, None, None

            except ValueError:
                tk.Label(root, text="Please enter valid numbers", font=("Helvetica", 14)).pack()
                return False, None, None

        # Create entry boxes asking for number of point loads and distributed loads
        
        
        if self.current_frame:
            self.current_frame.destroy()
        label1 = tk.Label(root, text="How many point loads does this bridge hold?", font=("Helvetica", 14))
        label1.pack()
        entry1 = tk.Entry(root, font=("Helvetica", 14))
        entry1.insert(0, "0")
        entry1.pack()
        tk.Label(root, text="").pack()

        label2 = tk.Label(root, text="How many distributed loads does this bridge hold?", font=("Helvetica", 14))
        label2.pack()
        entry2 = tk.Entry(root, font=("Helvetica", 14))
        entry2.insert(0, "0")
        entry2.pack()
        tk.Label(root, text="").pack()

        def handle_button_click():
            if get_numbers()[0]:
                print("Kiraly")
            else:
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry1.insert(0, "Enter valid numbers")
                entry2.insert(0, "Enter valid numbers")
            # Create button to submit entered numbers
        button = tk.Button(root, text="Enter", command=handle_button_click)
        button.pack()

    def calculate_menu2(self, num_point_loads):
        if self.current_frame:
            self.current_frame.destroy()

        def print_numbers():
            for number in point_weights:
                print(number)

        point_weights = []

        for i in range(num_point_loads):
            label = tk.Label(self.current_frame, text=f"Point Load {i+1}:", font=("Helvetica", 14))
            label.pack()
            entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
            entry.insert(0, "0")
            entry.pack()
            point_weights.append(entry)

        # Create button to submit entered numbers
        button = tk.Button(root, text="Enter", command=print_numbers)
        button.pack()

    def change_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()
        
        tk.Button(self.current_frame, text="A", command=self.display_message('A'), font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=30)
        tk.Button(self.current_frame, text="Back", command=self.main_menu).pack(pady=30)

    def display_message(self, message):
        def callback():
            print(message)
        return callback

root = tk.Tk()
app = Menu(root)
root.mainloop()