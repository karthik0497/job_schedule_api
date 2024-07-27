import time
import requests
import urllib3
urllib3.disable_warnings()



API_ACCESS_TOKEN = '123456'
headers_dict = {'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(API_ACCESS_TOKEN)}


def call_rest_api(request_type, endpoint, data=None, params=None, no_token=False, num_tries=10):
    PRINTINFO, REQUESTS_TIMEOUT, api_failure_count = True, 60, 0
    api_response = {"status": "failure", "statusbool": False}
    for i in range(num_tries):
        try:
            url = endpoint
            if request_type == "get":
                if no_token:
                    api_response = requests.get(url, params=params, verify=False, timeout=REQUESTS_TIMEOUT)
                else:
                    api_response = requests.get(url, params=params, verify=False, timeout=REQUESTS_TIMEOUT, headers=headers_dict)
            elif request_type == "post":
                api_response = requests.post(url, data=data, params=params, verify=False, timeout=REQUESTS_TIMEOUT, headers=headers_dict)
            elif request_type == "patch":
                api_response = requests.patch(url, data=data, params=params, verify=False, timeout=REQUESTS_TIMEOUT, headers=headers_dict)
            elif request_type == "delete":
                api_response = requests.delete(url, params=params, verify=False, timeout=REQUESTS_TIMEOUT, headers=headers_dict)
                return api_response
            else:
                print("call_rest_api - ERROR - unknown request_type")
                return api_response
            print(api_response.url)
            return api_response.json()

        except Exception as e:
            print("Internet Connection error occurred, retrying ....", e)
            time.sleep(3)
        api_failure_count += 1



