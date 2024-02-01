#!/usr/bin/env python3

import sys
import endurox as e
import tx_fields as t

class Server:

    def tpsvrinit(self, args):
        e.tplog_info("Doing server init...");
        e.tpadvertise("CREATE_TRANSACTION", "CREATE_TRANSACTION", Server.CREATE_TRANSACTION)
        e.tpadvertise("CREDITDEBIT", "CREDITDEBIT", Server.CREDITDEBIT)
        return 0

    def tpsvrdone(self):
        e.tplog_info("Server shutdown")

    def CREATE_TRANSACTION(self, args):
        #e.tplogprintubf(e.log_info, "Incoming request:", args.data)
        args.data["data"] = {
        t.tx_access_token: "23421adad12321adssd",
        t.tx_token_type: "Bearer",
        t.tx_expires_in: 2399,
        t.tx_status: "awaiting_authorisation",
        t.tx_creation_date: 1231313131,
        t.tx_expiration_date: 1231313431,
        t.tx_consent_id: "id",
        t.tx_account_id: "account_id",
        t.tx_account_type: "Personal",
        t.tx_account_subtype: "Current",
        t.tx_nickname: "Bills",
        t.tx_bank_name: "bank_name",
        t.tx_verified: 0,
        t.tx_countries: ["EU"],
        t.tx_developer_portal: "testbank.com",
        t.tx_label: "transaction init",
        t.tx_premium: 0,
        t.tx_categories: "accounts",
        t.tx_documentation_url: "docurl.com",
        t.tx_blocked: 0,
        t.tx_bank_swift: "bank_swift",
        t.tx_balance_available: 259.33,
        t.tx_limit: 750,
        t.tx_amount: 39.95,
        t.tx_currency: "EUR",
        t.tx_transaction_details: "transaction_details",
        t.tx_country: "DE",
        t.tx_city: "city",
        t.tx_street: "street",
        t.tx_street_number: "street_number",
        t.tx_apt_number: 4,
        t.tx_debit_response_code: 0,
        t.tx_credit_respoonse_code: 0,
        t.tx_test: 0,
        t.tx_fee: 0,
        t.tx_source_order_id: None,
        t.tx_credit_exceeded: 0,
        t.tx_merchant: "Example Mart",
        t.tx_account_number: "**** **** **** 1234",
        t.tx_transaction_type: "Debit",
        t.tx_category: "Retail",
        t.tx_location: "Berlin, DE",
        t.tx_payment_method: "Credit Card",
        t.tx_card_type: "Visa",
        t.tx_card_last_digits: "4321",
        t.tx_authorization_code: "AUTH500",
        t.tx_is_expense_reported: 1,
        t.tx_is_receipt_attached: 1,
        t.tx_is_pending: 1,
        t.tx_is_duplicate: 0,
        t.tx_is_recurring: 0,
        t.tx_is_anomaly: 0,
        t.tx_is_flagged: 0,
        t.tx_beneficiary_name: "Test Customer",
        t.tx_beneficiary_account: "Test account",
        t.tx_beneficiary_bank: "Example Bank",
        t.tx_tax_amount: 2.39,
        t.tx_tax_rate: 19,
        t.tx_fee_amount: 2.50,
        t.tx_fee_description: "Transaction Fee",
        t.tx_insurance_policy: "pol23",
        t.tx_device_type: "mobile",
        t.tx_ip_address: "192.168.2.1",
        t.tx_browser: "mobile",
        t.tx_os: "android",
        t.tx_is_fraudulent: 0,
        t.tx_related_transactions: ["TRANS1", "TRANS2"],
        t.tx_test_field2: "value2",
        t.tx_test_field1: "value1",
        t.tx_test_field3: "value3",
        t.tx_test_field4: "value4",
        t.tx_test_field5: "value5",
        t.tx_test_field6: "value6",
        t.tx_test_field7: "value7",
        t.tx_test_field8: "value8",
        t.tx_test_field9: "value9",
        t.tx_test_field10: "value10",
        t.tx_test_field11: "value11",
        t.tx_test_field12: "value12",
        t.tx_test_field13: "value13",
        t.tx_test_field14: "value14",
        t.tx_test_field15: "value15",
        t.tx_test_field16: "value16",
        t.tx_test_field17: "value17",
        t.tx_test_field18: "value18",
        t.tx_test_field19: "value19",
        t.tx_test_field20: "value20",
        t.tx_test_field21: "value1",
        t.tx_test_field22: "value2",
        t.tx_test_field23: "value3",
        t.tx_test_field24: "value4",
        t.tx_test_field25: "value5",
        t.tx_test_field26: "value6",
        t.tx_test_field27: "value7",
        t.tx_test_field28: "value8",
        t.tx_test_field29: "value9",
        t.tx_test_field30: "value10",
        t.tx_test_field31: "value11",
        t.tx_test_field32: "value12",
        t.tx_test_field33: "value13",
        t.tx_test_field34: "value14",
        t.tx_test_field35: "value15",
        t.tx_test_field36: "value16",
        t.tx_test_field37: "value17",
        t.tx_test_field38: "value18",
        t.tx_test_field39: "value19",
        t.tx_test_field40: "value20",
    }
        # args.data["data"]["T_STRING_2_FLD"]="Hello World from XATMI server"
        return e.tpreturn(e.TPSUCCESS, 0, args.data)

    def CREDITDEBIT(self, args):
        return e.tpforward("DEBIT", args.data)

if __name__ == "__main__":
    e.tprun(Server(), sys.argv)
