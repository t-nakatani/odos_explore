import time
from datetime import datetime
import json
import requests
from web3 import Web3

class AddressConverter:
    def __init__(self):
        self.w3 = Web3()

    def to_checksum_address(self, address):
        return self.w3.to_checksum_address(address)

class QuoteService:
    def __init__(self, quote_url, converter):
        self.quote_url = quote_url
        self.converter = converter
        self.headers = {"Content-Type": "application/json"}

    def create_quote_request(self, chain_id, input_token, input_amount, output_token, slippage, user_addr, referral_code=0, disable_rfqs=True, compact=True):
        return {
            "chainId": chain_id,
            "inputTokens": [
                {
                    "tokenAddress": self.converter.to_checksum_address(input_token),
                    "amount": str(input_amount)
                }
            ],
            "outputTokens": [
                {
                    "tokenAddress": self.converter.to_checksum_address(output_token),
                    "proportion": 1
                }
            ],
            "slippageLimitPercent": slippage,
            "userAddr": self.converter.to_checksum_address(user_addr),
            "referralCode": referral_code,
            "disableRFQs": disable_rfqs,
            "compact": compact,
        }

    def get_quote(self, request_body):
        response = requests.post(self.quote_url, headers=self.headers, json=request_body)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Error in Quote: {response.json()}")

# 使い方
converter = AddressConverter()
quote_service = QuoteService("https://api.odos.xyz/sor/quote/v2", converter)

# トークンアドレスとその他の情報
USDC = "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e"
zUSDC = "0x474bb79c3e8e65dcc6df30f9de68592ed48bbfdb"
user_addr = "0x81263f67a6354e58C54f485963ebcb6058422940"

# リクエストを作成
quote_request = quote_service.create_quote_request(
    chain_id=43114,
    input_token=USDC,
    input_amount=100 * 10 ** 6,
    output_token=zUSDC,
    slippage=0.3,
    user_addr=user_addr
)
while(1):
    time.sleep(60)
    # クォートを取得
    try:
        quote = quote_service.get_quote(quote_request)
        print(f'[{datetime.now()}]\n{quote}\n')
    except ValueError as e:
        print(str(e))
    
