# plot_shower_class.py

from tp_utils import *

class PlotShower:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitcoin Prices Plot")

        # Log "STARTING" event with timestamp
        logging.info("GUI is starting.")

        # Add a label
        label = Label(root, text="Click the button to create and show the Bitcoin prices plot.")
        label.pack()

        # Add a button to trigger the plot creation and show it in a new window
        button_create_plot = Button(root, text="Show Plot", command=self.create_and_show_plot)
        button_create_plot.pack()

        # Add a button to quit the GUI
        button_quit = Button(root, text="Quit", command=self.quit_gui)
        button_quit.pack()

    def create_and_show_plot(self):
        try:
            # Dummy data for testing
            timestamps = [1637971200000, 1638057600000, 1638144000000]
            prices = [50000, 55000, 52000]

            # Plotting
            fig, ax = plt.subplots()
            ax.plot(timestamps, prices, marker='o', linestyle='-')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price')
            ax.set_title('Bitcoin Prices Over Time')
            ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

            # Embed the plot in a tkinter window
            window = Toplevel(self.root)
            window.title("Bitcoin Prices Plot")

            # Embed the plot in the tkinter window
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack()

            # Run the tkinter main loop for the new window
            window.mainloop()

        except Exception as e:
            # Log the exception with timestamp
            logging.error(f"An error occurred: {e}", exc_info=True)
            messagebox.showerror("Error", f"An error occurred: {e}")

    def quit_gui(self):
        # Log "QUIT" event with timestamp
        logging.info("Application is quitting.")

        self.root.quit()
        self.root.destroy()
        sys.exit(0)  # Use sys.exit() to forcefully exit the script

# Example of how to use the class
if __name__ == "__main__":
    root = Tk()
    app = PlotShower(root)
    root.mainloop()

