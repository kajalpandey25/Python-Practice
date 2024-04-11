# import requests
# import json

# query = input("What type of news are you interested in? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=ae2b8d2a1d484fabb3f9fc3915ab4495"
# r = requests.get(url)
# news = json.loads(r.text)
# # print(news, type(news))
# for article in news["articles"]:
#   print(article["title"])
#   print(article["description"])
#   print("--------------------------------------")
  
import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=ae2b8d2a1d484fabb3f9fc3915ab4495"
r = requests.get(url)
data = r.json()

if 'articles' in data:
    for article in data["articles"]:
        print(article.get("title", "No title available"))
        print(article.get("description", "No description available"))
        print("--------------------------------------")
else:
    print("No articles found for the given query.")
