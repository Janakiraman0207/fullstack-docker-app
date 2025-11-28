from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/products")
def products():
    data = [
        {"id": 1, "name": "MacBook Pro", "price": 125000, "img": "https://i.imgur.com/8Km9tLL.jpeg"},
        {"id": 2, "name": "Sony Headphones", "price": 7990, "img": "https://i.imgur.com/QrK5o2j.jpeg"},
        {"id": 3, "name": "Samsung Watch", "price": 19999, "img": "https://i.imgur.com/vZPjG6n.jpeg"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
