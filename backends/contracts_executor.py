import requests

"""
Wrapper to call contract-executor - https://github.com/shuva10v/contracts-executor
"""
class ContractsExecutor:
    def __init__(self, api_url):
        self.api_url = api_url

    def execute(self, code, data, address, method, types):
        request = {'code': code, 'data': data, 'method': method,
               'expected': types, 'address': address, 'arguments': []}
        res = requests.post(self.api_url, json=request)
        return res.json()['result']

    def get_wallet_balance(self, address):
        method = 'get_wallet_balance'
        types = ['int']
        request = {'address': address, 'method': method, 'expected': types, 'arguments': []}
        res = requests.post(self.api_url, json=request)
        return res.json()['result'][0]
