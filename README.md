# 📘 Contact Book Project

A simple command-line contact management application built with Python.
This project allows you to add, view, update, and delete contact information (name, phone number, and email) easily through a text-based interface.

---
## 🧠 Features

- ➕ Add new contacts with phone numbers and email addresses

- ✏️ Edit existing contacts (replace or add new information)

- 👁️ View a specific contact or all saved contacts in a table

- ❌ Delete contacts

- 💾 Auto-save all contacts into a contact_book.txt file upon exit

- 📋 Beautiful tabular display using the PrettyTable library

---
## 🧩 Project Structure
```bash
Contact-Book-Project/
│
├── src/
│   ├── main.py          # Core ContactBook class implementation
│   ├── run.py           # Command-line interface logic
│
├── README.md            # Project documentation
├── requirements.txt     # Dependencies list
└── contact_book.txt     # Output file (created at runtime)
```

---
## ⚙️ Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/maryamtaherifar/Contact-Book-Project.git
```
2. Move into the project directory
```bash
cd Contact-Book-Project
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
---
## ▶️ How to Run

Navigate to the src/ folder and run the app:
```bash
cd src
python run.py
```
Then follow the on-screen instructions to manage your contacts.
When you exit, all contacts will be saved automatically in contact_book.txt.
