from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"response":"testok"})

@app.route('/debit', methods=['POST'])
def post_data():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({'error': 'Invalid JSON'}), 400

        data["tx_debit"] = "passed"

        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# if __name__ == '__main__':
#     app.run(debug=True, port=3002)
# gunicorn --bind 0.0.0.0:3002 -w 8 wsgi:app
