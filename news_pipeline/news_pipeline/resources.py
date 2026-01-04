import random
from datetime import datetime
from dagster import resource


class NewsAPIClient:
    def __init__(self, default_limit: int):
        self.default_limit = default_limit


    def fetch_articles(self, limit: int | None = None):
        final_limit = limit or self.default_limit
        articles = []

        for i in range(final_limit):
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




@resource(
    config_schema={
        "default_limit": int,
    }
)
def news_api_resource(context):
    return NewsAPIClient(
        default_limit=context.resource_config["default_limit"]
    )