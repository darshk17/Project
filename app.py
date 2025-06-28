from flask import Flask, jsonify, request, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'supersecretkey'
CORS(app)

products = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 15}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    item = request.json
    cart = session.get("cart", [])
    cart.append(item)
    session["cart"] = cart
    return jsonify({"message": "Added to cart", "cart": cart})

@app.route("/cart", methods=["GET"])
def view_cart():
    return jsonify(session.get("cart", []))

if __name__ == "__main__":
    app.run(debug=True)
