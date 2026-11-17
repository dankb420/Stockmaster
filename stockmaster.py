"""StockMaster - a barebones inventory app.

Type in an item code, name, price and stock. Each item is saved to
SQLite (stock.db) and listed in the table below.
"""
import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

try:  # keeps text crisp on high-DPI Windows screens
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stock.db")
FIELDS = ["Item Code", "Item Name", "Item Price", "Item Stock"]

class StockApp:
    def __init__(self, root):
        self.root = root
        root.title("StockMaster")

        # database
        self.db = sqlite3.connect(DB_FILE)
        self.db.execute("CREATE TABLE IF NOT EXISTS items ("
                        "code TEXT PRIMARY KEY, name TEXT, "
                        "price REAL, stock INTEGER)")

        # input form
        form = ttk.Frame(root, padding=12)
        form.pack(fill="x")
        self.entries = []
        for col, label in enumerate(FIELDS):
            ttk.Label(form, text=label).grid(row=0, column=col, sticky="w", padx=4)
            entry = ttk.Entry(form, width=16)
            entry.grid(row=1, column=col, padx=4, pady=(2, 0))
            self.entries.append(entry)
        ttk.Button(form, text="Add Item", command=self.add_item).grid(row=1, column=4, padx=8)

        # output table
        self.table = ttk.Treeview(root, columns=FIELDS, show="headings", height=10)
        for label in FIELDS:
            self.table.heading(label, text=label)
            self.table.column(label, width=130)
        self.table.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        root.bind("<Return>", lambda event: self.add_item())
        self.show_items()

    def add_item(self):
        code, name, price, stock = [e.get().strip() for e in self.entries]
        if not code or not name:
            messagebox.showerror("Error", "Item code and name are required.")
            return
        try:
            price, stock = float(price), int(stock)
            if price < 0 or stock < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Price and stock must be positive numbers.")
            return
        try:
            self.db.execute("INSERT INTO items VALUES (?, ?, ?, ?)",
                            (code, name, price, stock))
            self.db.commit()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "That item code already exists.")
            return
        for entry in self.entries:
            entry.delete(0, "end")
        self.show_items()

    def show_items(self):
        self.table.delete(*self.table.get_children())
        rows = self.db.execute("SELECT code, name, price, stock FROM items ORDER BY code")
        for code, name, price, stock in rows:
            self.table.insert("", "end", values=(code, name, f"{price:.2f}", stock))


if __name__ == "__main__":
    root = tk.Tk()
    StockApp(root)
    root.mainloop()
