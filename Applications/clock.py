import tkinter as tk  # Import tkinter for GUI elements
import datetime  # Import datetime for time functionality

class DigitalClock(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tkinter window
        self.title("Digital Clock")  # Set the window title

        self.time_label = tk.Label(self, font=("Arial", 36), bg="black", fg="white")  # Create a label for time display
        self.time_label.pack(fill=tk.BOTH, expand=True)  # Pack the label to fill the window

        self.update_time()  # Call the update_time function initially

    def update_time(self):
        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.config(text=formatted_time)  # Update the label text

        self.after(1000, self.update_time)  # Schedule next update in 1 second

if __name__ == "__main__":
    clock = DigitalClock()
    clock.mainloop()  # Start the main event loop

Explanation of Improvements:
 * tkinter as tk: Imports tkinter as tk for cleaner code.
 * DigitalClock Class: Encapsulates the clock logic in a class for better organization and reusability.
 * __init__(): Initializes the class, creates the Tkinter window, sets the title, and creates the time label. Sets the font, background, and foreground colors for better aesthetics. Packs the label to fill the window. Calls the update_time() function initially to start displaying the current time.
 * update_time() Function: Updates the time_label with the current time formatted using datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"). Schedules the next update using self.after(1000, self.update_time) to call the function again after 1000 milliseconds (1 second).
 * if __name__ == "__main__": Block: Ensures the code within this block only executes when the script is run directly, not when imported as a module. Creates an instance of the DigitalClock class and starts the main event loop with mainloop().
