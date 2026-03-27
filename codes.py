import tkinter as tk
import time  # used to track time

# List of students
students = ["Ali", "Ayşe", "Mehmet"]

attendance = {}  # stores attendance data (name: status)
labels = {}      # stores label widgets for each student

start_time = time.time()  # record the time when program starts

# Function to determine status based on elapsed time
def get_status():
    elapsed = time.time() - start_time  # time passed (in seconds)

    if elapsed < 10:
        return "Present"   # first 10 seconds
    elif elapsed < 20:
        return "Late"      # between 10-20 seconds
    else:
        return "Absent"    # after 20 seconds

# Called when button is pressed
def mark(name):
    status = get_status()  # get current status
    attendance[name] = status  # save it

    # Update the label text on screen
    labels[name].config(text=f"{name}: {status}")

# Updates the "current status" label every second
def update_timer():
    status = get_status()
    timer_label.config(text=f"Current Status: {status}")

    # Call this function again after 1 second (loop)
    root.after(1000, update_timer)

# Create main window
root = tk.Tk()
root.title("Smart Attendance System")

# Top label showing current global status
timer_label = tk.Label(root, text="", font=("Arial", 12))
timer_label.pack(pady=10)

# Frame to hold student rows
frame = tk.Frame(root)
frame.pack()

# Create UI row for each student
for student in students:
    row = tk.Frame(frame)
    row.pack(pady=5)

    # Label showing student status
    lbl = tk.Label(row, text=f"{student}: Not Marked", width=20)
    lbl.pack(side="left")
    labels[student] = lbl  # store label reference

    # Button to mark attendance
    btn = tk.Button(row, text="Mark",
                    command=lambda s=student: mark(s))
    btn.pack(side="left", padx=5)

# Start timer updates
update_timer()

# Run the application
root.mainloop()
