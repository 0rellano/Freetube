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

@pytest.mark.parametrize(
        "entry_input", [
            "Texto de Prueba",
            "23/12/10",
            "",
        ]
)
def test_get_url(entry_input):
    app = MainWindow()

    app.entry_url.delete(0, tk.END)
    app.entry_url.insert(0, entry_input)
    
    app.button_url.invoke()

    assert app.get_video() == entry_input
