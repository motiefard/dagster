import random
from datetime import datetime
from dagster import resource


class NewsAPIClient:
    def fetch_articles(self, limit: int = 5):
        """
        Fake API
        """
        articles = []

        for i in range(limit):
            articles.append(
                {
                    "id": i,
                    "title": f"News Title {i}",
                    "content": "Dagster makes data pipelines reliable.",
                    "published_at": datetime.utcnow().isoformat(),
                    "source": random.choice(["BBC", "CNN", "Al Jazeera"]),
                }
            )

        return articles




@resource
def news_api_resource():
    return NewsAPIClient()