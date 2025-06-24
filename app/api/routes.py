from flask import Flask, request, jsonify
from flasgger import Swagger
from services.finance import calculate_rentability, testing_get, crypto_price
app = Flask(__name__)
swagger = Swagger(app)

app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/api/testing', methods=['GET'])
def testing():
    """
    A simple test endpoint to verify the API is working.
    """
    return jsonify({"message": "API is working!"})

@app.route('/api/echo', methods=['POST'])
def echo():
    """
    An endpoint that echoes back the JSON data sent to it.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify(data)

@app.route('/api/crypto_price', methods=['GET'])
def crypto_price_api():
    """
    Fetch the current cryptocurrency prices.
    ---
    tags:
      - Crypto
    responses:
      200:
        description: A list of cryptocurrency prices
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: object
                properties:
                  name:
                    type: string
                    example: Bitcoin
                  price:
                    type: number
                    example: 45000.0
      500:
        description: Error fetching crypto prices
    """
    try:
        data = crypto_price()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/rentability', methods=['POST'])
def rentability_api():
    """
    Calculate the rentability based on the provided parameters.
    ---
    tags:
      - Rentability
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            n_price:
              type: number
              example: 10.0
            actual_price:
              type: number
              example: 15.0
            n_quantity:
              type: number
              example: 100
            actual_quantity:
              type: number
              example: 100
    responses:
      200:
        description: Rentability calculated
        schema:
          type: object
          properties:
            rentability:
              type: number
              example: 0.5
      400:
        description: Invalid input
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    try:
        n_price = float(data.get('n_price'))
        actual_price = float(data.get('actual_price'))
        n_quantity = float(data.get('n_quantity'))
        actual_quantity = float(data.get('actual_quantity'))

        rentability = calculate_rentability(n_price, actual_price, n_quantity, actual_quantity)
        return jsonify({"rentability": rentability}), 200

    except (ValueError, TypeError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/testing', methods=['GET'])
def testing_get_api():
    """
    A test endpoint to verify the finance service is working.
    ---
    tags:
      - Finance
    responses:
      200:
        description: Test response from the finance service
        schema:
          type: object
          properties:
            message:
              type: string
              example: This is a test response from the finance service.
    """
    return jsonify(testing_get()), 200
    
class api:
    app = app