from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests, json

# Create your views here.
@api_view(['POST'])
def create_transaction(request):
    data = {
        "tx_access_token": "23421adad12321adssd",
        "tx_token_type": "Bearer",
        "tx_expires_in": 2399,
        "tx_status": "awaiting_authorisation",
        "tx_creation_date": 1231313131,
        "tx_expiration_date": 1231313431,
        "tx_consent_id": "id",
        "tx_account_id": "account_id",
        "tx_account_type": "Personal",
        "tx_account_subtype": "Current",
        "tx_nickname": "Bills",
        "tx_bank_name": "bank_name",
        "tx_verified": False,
        "tx_countries": ["EU"],
        "tx_developer_portal": "testbank.com",
        "tx_label": "transaction init",
        "tx_premium": False,
        "tx_categories": "accounts",
        "tx_documentation_url": "docurl.com",
        "tx_blocked": False,
        "tx_bank_swift": "bank_swift",
        "tx_balance_available": 259.33,
        "tx_limit": 750,
        "tx_amount": 39.95,
        "tx_currency": "EUR",
        "tx_transaction_details": "transaction_details",
        "tx_country": "DE",
        "tx_city": "city",
        "tx_street": "street",
        "tx_street_number": "street_number",
        "tx_apt_number": 4,
        "tx_debit_response_code": 0,
        "tx_credit_respoonse_code": 0,
        "tx_test": False,
        "tx_fee": 0,
        "tx_source_order_id": None,
        "tx_credit_exceeded": False,
        "tx_merchant": "Example Mart",
        "tx_account_number": "**** **** **** 1234",
        "tx_transaction_type": "Debit",
        "tx_category": "Retail",
        "tx_location": "Berlin, DE",
        "tx_payment_method": "Credit Card",
        "tx_card_type": "Visa",
        "tx_card_last_digits": "4321",
        "tx_authorization_code": "AUTH500",
        "tx_is_expense_reported": True,
        "tx_is_receipt_attached": True,
        "tx_is_pending": True,
        "tx_is_duplicate": False,
        "tx_is_recurring": False,
        "tx_is_anomaly": False,
        "tx_is_flagged": False,
        "tx_beneficiary_name": "Test Customer",
        "tx_beneficiary_account": "Test account",
        "tx_beneficiary_bank": "Example Bank",
        "tx_tax_amount": 2.39,
        "tx_tax_rate": 19,
        "tx_fee_amount": 2.50,
        "tx_fee_description": "Transaction Fee",
        "tx_insurance_policy": "pol23",
        "tx_device_type": "mobile",
        "tx_ip_address": "192.168.2.1",
        "tx_browser": "mobile",
        "tx_os": "android",
        "tx_is_fraudulent": False,
        "tx_related_transactions": ["TRANS1", "TRANS2"],
        "tx_test_field2": "value2",
        "tx_test_field1": "value1",
        "tx_test_field3": "value3",
        "tx_test_field4": "value4",
        "tx_test_field5": "value5",
        "tx_test_field6": "value6",
        "tx_test_field7": "value7",
        "tx_test_field8": "value8",
        "tx_test_field9": "value9",
        "tx_test_field10": "value10",
        "tx_test_field11": "value11",
        "tx_test_field12": "value12",
        "tx_test_field13": "value13",
        "tx_test_field14": "value14",
        "tx_test_field15": "value15",
        "tx_test_field16": "value16",
        "tx_test_field17": "value17",
        "tx_test_field18": "value18",
        "tx_test_field19": "value19",
        "tx_test_field20": "value20",
        "tx_test_field21": "value1",
        "tx_test_field22": "value2",
        "tx_test_field23": "value3",
        "tx_test_field24": "value4",
        "tx_test_field25": "value5",
        "tx_test_field26": "value6",
        "tx_test_field27": "value7",
        "tx_test_field28": "value8",
        "tx_test_field29": "value9",
        "tx_test_field30": "value10",
        "tx_test_field31": "value11",
        "tx_test_field32": "value12",
        "tx_test_field33": "value13",
        "tx_test_field34": "value14",
        "tx_test_field35": "value15",
        "tx_test_field36": "value16",
        "tx_test_field37": "value17",
        "tx_test_field38": "value18",
        "tx_test_field39": "value19",
        "tx_test_field40": "value20",
    }
    return Response(data)

@api_view(['POST'])
def creditdebit(request):
    data = request.data
    if not data:
        return Response({'error': 'Invalid JSON in request body'}, 400)
    
    headers = {"Content-type": "application/json"}

    debit = requests.post(
        "http://localhost:3002/debit", data=json.dumps(data), headers=headers)
    debitResponse = debit.json()

    if debitResponse["tx_debit"] != "passed":
        print("Debit NOT verified, sending request to credit")

    credit = requests.post("http://localhost:3001/credit", data=json.dumps(
        debitResponse), headers=headers)
    creditResponse = credit.json()
    if creditResponse["tx_credit"] != "passed":
        print("Credit NOT verified, sending request to credit")

    return Response(creditResponse)