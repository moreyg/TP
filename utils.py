# utils.py
import sys
import logging
from tkinter import Tk, Label, Button, Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.info("Logging has been set up.")

def create_tkinter_root():
    return Tk()

