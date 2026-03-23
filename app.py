from flask import Flask, render_template, request, jsonify
from database import init_db, get_db

app = Flask(__name__)

with app.app_context():
    init_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/books", methods=["GET"])
def get_books():
    query = request.args.get("q", "").strip()
    db = get_db()
    if query:
        books = db.execute(
            """SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ? OR genre LIKE ?
        ORDER BY created_at DESC""",
            (f"%{query}%", f"%{query}%", f"%{query}%"),
        ).fetchall()
    else:
        books = db.execute(
            "SELECT * FROM books ORDER BY created_at DESC"
        ).fetchall()
    return jsonify([dict(b) for b in books])


@app.route("/api/books", methods=["POST"])
def add_book():
    data   = request.get_json()
    title  = data.get("title", "").strip()
    author = data.get("author", "").strip()
    genre  = data.get("genre", "").strip()
    year   = data.get("year", "").strip()
    status = data.get("status", "Available")

    if not title or not author:
        return jsonify({"error": "Title and Author are required."}), 400

    db = get_db()
    db.execute(
        "INSERT INTO books (title, author, genre, year, status) VALUES (?, ?, ?, ?, ?)",
        (title, author, genre, year, status),
    )
    db.commit()
    return jsonify({"message": "Book added!"}), 201


@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data   = request.get_json()
    title  = data.get("title", "").strip()
    author = data.get("author", "").strip()
    genre  = data.get("genre", "").strip()
    year   = data.get("year", "").strip()
    status = data.get("status", "Available")

    if not title or not author:
        return jsonify({"error": "Title and Author are required."}), 400

    db = get_db()
    db.execute(
        "UPDATE books SET title=?, author=?, genre=?, year=?, status=? WHERE id=?",
        (title, author, genre, year, status, book_id),
    )
    db.commit()
    return jsonify({"message": "Book updated!"})


@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    db = get_db()
    db.execute("DELETE FROM books WHERE id=?", (book_id,))
    db.commit()
    return jsonify({"message": "Book deleted."})


@app.route("/api/stats", methods=["GET"])
def stats():
    db = get_db()
    total     = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
    available = db.execute("SELECT COUNT(*) FROM books WHERE status='Available'").fetchone()[0]
    issued    = db.execute("SELECT COUNT(*) FROM books WHERE status='Issued'").fetchone()[0]
    genres    = db.execute("SELECT COUNT(DISTINCT genre) FROM books WHERE genre != ''").fetchone()[0]
    return jsonify({"total": total, "available": available, "issued": issued, "genres": genres})


if __name__ == "__main__":
    app.run(debug=True)
