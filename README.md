# StockMaster
A GUI Implementation group project to understand the usage of tkinter library in python and utilize it to solve a daily problem.
StockMaster

A lightweight inventory management application built with Python, Tkinter, and SQLite.

Features

- Add inventory items with unique item codes.
- Store item names, prices, and stock quantities.
- View inventory records in a tabular interface.
- Validate user inputs and prevent duplicate entries.
- Automatically save records using SQLite.
- Load existing inventory data on startup.

Tech Stack

- Python – Application logic
- Tkinter – Graphical user interface
- SQLite3 – Database management

Installation

Clone the repository:

git clone https://github.com/dankb420/Stockmaster.git
cd Stockmaster

Run the application:

python stockmaster.py

No external Python packages are required.

Database

The application automatically creates "stock.db" and maintains an "items" table containing:

- "code" – Unique item identifier
- "name" – Item name
- "price" – Item price
- "stock" – Available quantity

Future Improvements

- Edit and delete inventory items.
- Search and filter records.
- Low-stock notifications.
- Export inventory data.

License

Developed as an academic project.
