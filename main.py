import requests
import json

# Retrieved from https://codeburst.io/deep-dive-into-ethereum-logs-a8d2047c7371
TRANSFER_TOPIC = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
APPROVAL_TOPIC = '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925'

def rpc_call(method, args, url='http://localhost:8545'):
    json_data = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': method,
            'params': args
            }

    r = requests.post(url, json=json_data)

    return json.loads(r.text)
