# utils.py
import sys
import logging
import sqlite3
from tkinter import Tk, Label, Button, Toplevel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO


def setup_logging():
    # Create a logger
    logger = logging.getLogger('my_tp_app')
    logger.setLevel(logging.INFO)

    # Create handlers (console and file)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('tp_app.log')

    # Create formatters and add it to the handlers
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    c_handler.setFormatter(formatter)
    f_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

def create_tkinter_root():
    return Tk()
