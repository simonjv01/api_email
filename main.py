import requests

api_key = "fe467a8e2f144eff93ee6bcc33d5543f"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key

request = requests.get(url)

content = request.json()



print(content)
