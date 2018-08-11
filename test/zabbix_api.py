import requests, json

url = 'http://127.0.0.1/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
 