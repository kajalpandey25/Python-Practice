import requests

# Replace 'YOUR_API_KEY' with your actual NewsAPI key
API_KEY = 'ae2b8d2a1d484fabb3f9fc3915ab4495'

def fetch_news(topic):
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        articles = data['articles']
        for idx, article in enumerate(articles, start=1):
            print(f"{idx}. {article['title']}")
            print(article['url'])
            print()
    else:
        print("Failed to fetch news.")

if __name__ == "__main__":
    topics = ['technology', 'business', 'health', 'science', 'sports']
    
    for topic in topics:
        print(f"News related to {topic.capitalize()}:")
        fetch_news(topic)
        print('-' * 50)
