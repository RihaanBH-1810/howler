import requests

# Send a GET request to the specified URL
response = requests.get("http://lab.awh.zdresearch.com/chapter2/xvwa/vulnerabilities/stored_xss/")

# Access the cookies attribute of the response object to get the cookies
cookies = response.cookies

# Iterate over the cookies and print their name and value
for cookie in cookies:
    print("Name:", cookie.name)
    print("Value:", cookie.value)
