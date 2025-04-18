from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def mojastrona():
    return "To jest moja strona!"

@app.route('/hello/<name>')
def hello(name):
    return f"Cześć, {name}!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))
        total = num1 + num2
        prediction = 1 if total > 5.8 else 0

        return jsonify({
            "prediction": prediction,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })

    except (ValueError, TypeError):
        return jsonify({"error": "Błędne dane wejściowe"}), 400

if __name__ == '__main__':
    app.run()
