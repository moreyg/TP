
# main.py

from utils import *
from plot_shower_class import PlotShower

# Setup logging
setup_logging()


# Create the Tkinter root window and run the GUI
if __name__ == "__main__":
    logging.info('Main starting...')
    root = create_tkinter_root()
    app = PlotShower(root)
    root.mainloop()
