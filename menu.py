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
        
        tk.Button(self.current_frame, text="Calculate support reactions", command=self.calculate_menu, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=30)
        tk.Button(self.current_frame, text="Change default units of measurement", command=self.change_menu, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=30)
        tk.Button(self.current_frame, text="Exit", command=self.root.quit, font=("Helvetica", 24), bg="orange", fg="white", padx=20, pady=10).pack(pady=50)

    def calculate_menu(self):
        def get_numbers():
            try:
                point_loads = int(self.entry1.get())
                distributed_loads = int(self.entry2.get())

                if point_loads >= 0 and distributed_loads >= 0:
                    return True, point_loads, distributed_loads
                else:
                    return False, None, None
            except ValueError:
                tk.Label(self.current_frame, text="Please enter valid numbers", font=("Helvetica", 14)).pack()
                return False, None, None

        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        label1 = tk.Label(self.current_frame, text="How many point loads does this bridge hold?", font=("Helvetica", 14))
        label1.pack()
        self.entry1 = tk.Entry(self.current_frame, font=("Helvetica", 14))
        self.entry1.insert(0, "0")
        self.entry1.pack()
        tk.Label(self.current_frame, text="").pack()

        label2 = tk.Label(self.current_frame, text="How many distributed loads does this bridge hold?", font=("Helvetica", 14))
        label2.pack()
        self.entry2 = tk.Entry(self.current_frame, font=("Helvetica", 14))
        self.entry2.insert(0, "0")
        self.entry2.pack()
        tk.Label(self.current_frame, text="").pack()

        def handle_button_click():
            if get_numbers()[0]:
                self.calculate_menu2(get_numbers()[1], get_numbers()[2])
            else:
                self.entry1.delete(0, tk.END)
                self.entry2.delete(0, tk.END)
                self.entry1.insert(0, "Enter valid numbers")
                self.entry2.insert(0, "Enter valid numbers")

        button = tk.Button(self.current_frame, text="Enter", command=handle_button_click)
        button.pack()

    def calculate_menu2(self, num_point_loads, num_distributed_loads):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        point_weights = []
        distributed_weights = []

        for i in range(num_point_loads):
            label = tk.Label(self.current_frame, text=f"Point Load {i+1}:", font=("Helvetica", 14))
            label.pack()
            entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
            entry.insert(0, "0")
            entry.pack()
            point_weights.append(entry)

        for i in range(num_distributed_loads):
            label = tk.Label(self.current_frame, text=f"Distributed {i+1}:", font=("Helvetica", 14))
            label.pack()
            entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
            entry.insert(0, "0")
            entry.pack()
            distributed_weights.append(entry)

        def print_numbers():
            for entry in point_weights:
                print(entry.get())
            for entry in distributed_weights:
                print(entry.get())

        button = tk.Button(self.current_frame, text="Enter", command=print_numbers)
        button.pack()

    def change_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.main_menu()

root = tk.Tk()
app = Menu(root)
root.mainloop()