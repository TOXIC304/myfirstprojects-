import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the clock
clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="white")
clock_label.pack(padx=20, pady=20)

# Start the clock update function
update_clock()

# Run the application
root.mainloop()
