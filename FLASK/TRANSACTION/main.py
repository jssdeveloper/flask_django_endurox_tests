from flask import Flask, request, jsonify
import requests
import json
from dataset import example_data

app = Flask(__name__)

@app.route('/create_transaction', methods=['POST'])
def create():
    data = example_data
    try:
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/creditdebit', methods=['POST'])
def send_post_request():
    try:
        data = request.get_json()

        if data is None:
            return jsonify({'error': 'Invalid JSON in request body'}), 400

        headers = {"Content-type": "application/json"}

        debit = requests.post(
            "http://localhost:3002/debit", data=json.dumps(data), headers=headers)
        debitResponse = debit.json()

        if debitResponse["tx_debit"] != "passed":
            print("Debit NOT verified, sending request to credit")

        credit = requests.post("http://localhost:3001/credit", data=json.dumps(
            debitResponse), headers=headers)
        return credit.json()

    except Exception as e:
        return jsonify({'error': str(e)}), 500