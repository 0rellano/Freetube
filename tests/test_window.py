import pytest

import tkinter as tk
from src.gui.window import MainWindow



def test_window_instance():
    window = MainWindow()
    assert isinstance(window, tk.Tk)

def test_window_close():
    window = MainWindow()
    close = False
    window.destroy()
    try:
        window.winfo_exists(), "nose que poner acas"
    except:
        close = True
    assert close
