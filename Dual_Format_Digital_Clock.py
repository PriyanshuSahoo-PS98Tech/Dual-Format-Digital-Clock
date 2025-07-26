import tkinter as ui  # Importing Tkinter for GUI applications
import time  # Importing time module to retrieve system time

# Create the main window
window = ui.Tk()
window.title("Digital Clock") # Title
window.configure(bg="black") # Background color

# Function to update clock every second
def update_clock():
    format_12_hour = time.strftime("%I:%M:%S %p") # Fetching time in 12-hour format
    format_24_hour = time.strftime("%H:%M:%S")    # Fetching time in 24-hour format

    # Updating the lable texts with formatted time
    lbl_12.config(text=format_12_hour)
    lbl_24.config(text=format_24_hour)

    # Scheduling the function to run every 1 second
    window.after(1000, update_clock)

# Create heading
heading_12 = ui.Label(window, text="12-Hour Format Time", font=('Arial', 20, 'bold'),
                        background="black", foreground="deepskyblue")

heading_24 = ui.Label(window, text="24-Hour Format Time", font=('Arial', 20, 'bold'),
                        background="black", foreground="lawngreen")


# Create labels that will display the actual time
lbl_12 = ui.Label(window, text="00:00:00 AM", font=('Arial', 50, 'bold'),
                    background="black", foreground="white")

lbl_24 = ui.Label(window, text="00:00:00", font=('Arial', 50, 'bold'),
                    background="black", foreground="white")

# Arrange the Labels
heading_12.pack(pady=(15, 5)) # Adds vertical padding
lbl_12.pack(pady=5)

heading_24.pack(pady=(15, 5))
lbl_24.pack(pady=5)

# Update the clock
update_clock() # Function call

window.mainloop()