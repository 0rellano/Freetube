import tkinter as tk

class CustomEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color='gray', *args, **kwargs):
        super().__init__(master, *args, **kwargs) 

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_entry_focus_in)
        self.bind("<FocusOut>", self.on_entry_focus_out)

        self.put_placeholder()
    
    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def on_entry_focus_in(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, "end")
            self['fg'] = self.default_fg_color


    def on_entry_focus_out(self, event):
        if not self.get():
            self.put_placeholder()