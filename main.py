import requests

api_key = "fe467a8e2f144eff93ee6bcc33d5543f"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + api_key

request = requests.get(url)

content = request.json()

# print(content.keys())
# print(content["articles"][0].keys())
# print(content["articles"][0]["title"])
# print(content["articles"][0]["description"])
# print(content["articles"][0]["url"])
# print(content["articles"][0]["urlToImage"])

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print(article["urlToImage"])
    print("\n\n")


