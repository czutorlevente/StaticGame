import tkinter as tk
from calculator import Calculator
import objects

class Menu:
    # Store collected data
    point_weights = []
    point_distances = []

    distributed_weights = []
    distributed_distances = []

    point_load_objects = []
    distributed_load_objects = []

    weight_unit = "#"
    distance_unit = "feet"

    def point_load_saver(self, weight, distance):
        point_load = objects.PointLoad(weight.get(), distance.get())
        self.point_load_objects.append(point_load)
        root.quit()

    def distributed_load_saver(self, weight, distance, width):
        distributed_load = objects.DistributedLoad(weight.get(), distance.get(), width.get())
        self.distributed_load_objects.append(distributed_load)
        root.quit()

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

    #Widgets-----------------------------------
    def create_point_load_widgets(self, i, num_point_loads):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        #Ask for weight
        label = tk.Label(self.current_frame, text=f"Weight of Point Load {i+1}:", font=("Helvetica", 14))
        label.pack()
        entry_weight = tk.Entry(self.current_frame, font=("Helvetica", 14))
        entry_weight.pack()
            
        #Ask for distance
        label2 = tk.Label(self.current_frame, text=f"Distance of Point Load {i+1} from pillar 'A':", font=("Helvetica", 14))
        label2.pack()
        entry_distance = tk.Entry(self.current_frame, font=("Helvetica", 14))
        entry_distance.pack()

        #Save data
        button = tk.Button(self.current_frame, text="Enter", command=lambda weight=entry_weight, distance=entry_distance: self.point_load_saver(weight, distance))
        button.pack()

    def create_dist_load_widgets(self, i, num_distributed_loads):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        #Ask for width
        label = tk.Label(self.current_frame, text=f"Width of Distributed Load {i+1}:", font=("Helvetica", 14))
        label.pack()
        entry_width = tk.Entry(self.current_frame, font=("Helvetica", 14))
        entry_width.pack()
            
        #Ask for load amount
        label2 = tk.Label(self.current_frame, text=f"Load amount of Distributed Load {i+1}:", font=("Helvetica", 14))
        label2.pack()
        entry_weight = tk.Entry(self.current_frame, font=("Helvetica", 14))
        entry_weight.pack()
            
        #Ask for distance
        label3 = tk.Label(self.current_frame, text=f"Distance of closest end of Distributed {i+1} from pillar 'A':", font=("Helvetica", 14))
        label3.pack()
        entry_distance = tk.Entry(self.current_frame, font=("Helvetica", 14))
        entry_distance.pack()

        #Save data
        button = tk.Button(self.current_frame, text="Enter", command=lambda weight=entry_weight, distance=entry_distance, width=entry_width: self.distributed_load_saver(weight, distance, width))
        button.pack()

    #Menu 2 -------------------------------------
    def calculate_menu2(self, num_point_loads, num_distributed_loads):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()
        
        for i in range(num_point_loads):
            self.create_point_load_widgets(i, num_point_loads)
            root.mainloop()

        for i in range(num_distributed_loads):
            self.create_dist_load_widgets(i, num_distributed_loads)
            root.mainloop()
            

        for point_load in self.point_load_objects:
            weight = point_load.weight
            self.point_weights.append(weight)

            distance = point_load.distance
            self.point_distances.append(distance)

        for distrubuted_load in self.distributed_load_objects:
            weight = distrubuted_load.overall_weight
            self.distributed_weights.append(weight)

            distance = distrubuted_load.distance_point_eq
            self.distributed_distances.append(distance)
            
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = tk.Frame(self.root)
        self.current_frame.pack()

        label4 = tk.Label(self.current_frame, text=f"Distance of pillar B from pillar 'A':", font=("Helvetica", 16))
        label4.pack()
        entry_ab_distance = tk.Entry(self.current_frame, font=("Helvetica", 16))
        entry_ab_distance.insert(0, "0")
        entry_ab_distance.pack()


        def print_conclusion():
            # Store data
            ab_distance = float(entry_ab_distance.get())
            
            # Call support_reactions method
            all_weights = self.point_weights + self.distributed_weights
            all_distances = self.point_distances + self.distributed_distances
            support_A, support_B, end_line = Calculator.support_reactions("#", "feet", all_weights, all_distances, ab_distance)

            print(end_line)
            #conclusion_label = tk.Label(self.current_frame, text=end_line, font=("Helvetica", 16))
            #conclusion_label.pack()

        #Submit button
        button = tk.Button(self.current_frame, text="Calculate", command=print_conclusion)
        button.pack()

    def change_menu(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.main_menu()

root = tk.Tk()
app = Menu(root)
root.mainloop()
