import sqlite3
from flask import g, current_app

DB_PATH = "library.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            title      TEXT    NOT NULL,
            author     TEXT    NOT NULL,
            genre      TEXT    DEFAULT '',
            year       TEXT    DEFAULT '',
            status     TEXT    DEFAULT 'Available',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Seed sample data only when table is empty
    count = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    if count == 0:
        sample = [
            ("The Alchemist",          "Paulo Coelho",      "Fiction",    "1988", "Available"),
            ("Clean Code",             "Robert C. Martin",  "Technology", "2008", "Issued"),
            ("Sapiens",                "Yuval Noah Harari", "History",    "2011", "Available"),
            ("Atomic Habits",          "James Clear",       "Self-Help",  "2018", "Available"),
            ("The Great Gatsby",       "F. Scott Fitzgerald","Classic",   "1925", "Issued"),
            ("Introduction to Algorithms","Thomas Cormen",  "Technology", "1990", "Available"),
        ]
        db.executemany(
            "INSERT INTO books (title, author, genre, year, status) VALUES (?, ?, ?, ?, ?)",
            sample,
        )
    db.commit()
    db.close()
