import requests
import json
# Request Variables
uuid = 'e276abec-e0f2-11e3-8169-6d9ed49b625f'
access_token = '3d25ebe6-1bd9-459a-a17b-86024cfaa45c'
url = 'https://10.10.10.200/api/fmc_config/v1/domain/' + uuid + '/object/hosts'

# Request
headers = {'X-auth-access-token': access_token}
payload = {
          "name": "TestHost",
            "type": "Host",
              "value": "10.5.3.20",
                "description": "Test Description"
                }
r = requests.post(url, json=payload, headers=headers, verify=False)

print('\nStatus: ' + r.status_code + '\n\n')

pretty_json = json.loads(r.text)
print(json.dumps(pretty_json, indent=3))
