# 📚 Library Book Manager

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-black?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-3-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- ➕ **Add books** — title, author, genre, year, status
- 📋 **View all books** in a clean, sortable table
- ✏️ **Edit** any book's details
- 🗑️ **Delete** books with a confirmation prompt
- 🔍 **Search** by title, author, or genre
- 🏷️ **Status badges** — Available / Borrowed
- 💾 Persistent SQLite database (no setup needed)
- 📱 Responsive design

---

## 🗂️ Project Structure

```
library-book-manager/
├── app.py              # Flask routes & app config
├── database.py         # SQLite CRUD functions
├── requirements.txt    # Python dependencies
├── .gitignore
├── README.md
├── templates/
│   ├── base.html       # Shared layout
│   ├── index.html      # Book list + search
│   ├── add_book.html   # Add book form
│   └── edit_book.html  # Edit book form
└── static/
    └── css/
        └── style.css   # All styling
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/library-book-manager.git
cd library-book-manager
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Open your browser at **http://127.0.0.1:5000**

> The SQLite database (`library.db`) is created automatically on first run.

---

## 🛠️ Tech Stack

| Layer     | Technology        |
|-----------|-------------------|
| Backend   | Python 3, Flask   |
| Database  | SQLite (built-in) |
| Frontend  | HTML5, CSS3       |
| Templates | Jinja2 (Flask)    |

---

## 📸 Pages

| Route             | Description          |
|-------------------|----------------------|
| `/`               | All books + search   |
| `/add`            | Add a new book       |
| `/edit/<id>`      | Edit a book          |
| `/delete/<id>`    | Delete (POST only)   |
