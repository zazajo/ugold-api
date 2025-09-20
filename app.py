from flask import Flask, jsonify

app = Flask(__name__)

# Fixed supply values for Ceylon
TOTAL_SUPPLY = 4000000000000.0
CIRCULATING_SUPPLY = 3999894041550.31

@app.route('/totalsupply', methods=['GET'])
def get_total_supply():
    return jsonify(TOTAL_SUPPLY)

@app.route('/circulatingsupply', methods=['GET'])
def get_circulating_supply():
    return jsonify(CIRCULATING_SUPPLY)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug for production
