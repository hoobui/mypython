import requests, json

url = 'http://127.0.0.1/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}

data={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Zabbix server",
                "Linux server"
            ]
        }
    },
    "auth": "bfbdd0b61594f8c2fe87b72f2eb6bed5",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())