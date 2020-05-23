import requests
import pprint

print(requests.__file__)
url = "https://github_15.com/404"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.Timeout:
    print("Timeout error, url: ", url)
except requests.HTTPError as err:
    print("HTTP error: {0} {1}".format(url, err.response.status_code))
except requests.RequestException as err:
    print("Error occurred")
    print(err)
else:
    pprint.pprint(response.content)

