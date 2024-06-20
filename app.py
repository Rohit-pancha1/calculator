from flask import Flask, request, jsonify, render_template
import sympy as sp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    
    try:
        # Using sympy to evaluate the expression safely
        result = sp.sympify(expression)
        result = float(result.evalf())  # Converting the result to a float
        return jsonify(result=result)
    except Exception as e:
        return jsonify(result="Error"), 400

if __name__ == '__main__':
    app.run(debug=True)

