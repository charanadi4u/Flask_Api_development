from flask import Flask,session,request,jsonify

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/api/cart/add', methods=['POST'])
def add_to_cart():
    product_id = request.json.get('product_id')
    quantity = request.json.get('quantity', 1)
    # Assuming a structure for session['cart'] as a dictionary
    if 'cart' not in session:
        session['cart'] = {}
    if product_id in session['cart']:
        session['cart'][product_id]['quantity'] += quantity
    else:
        session['cart'][product_id] = {'quantity': quantity}
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)

