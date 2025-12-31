from dagster import asset, MetadataValue
from datetime import datetime

@asset(
    description="Raw news articles fetched from the News API",
    required_resource_keys={"news_api"},
)
def raw_news_articles(context):
    # fetch raw data
    articles = context.resources.news_api.fetch_articles(limit=5)

    # attach metadata
    context.add_output_metadata(
        {
            "article_count": len(articles),
            "fetched_at": datetime.utcnow().isoformat(),
            "sample_title": articles[0]["title"] if articles else "No data",
        }
    )

    return articles


@asset(
    description="cleaned and normalized",
)
def cleaned_news_articles(raw_news_articles):
    """transform data into clean format """
    
    cleaned = []

    for article in raw_news_articles:
        cleaned.append(
            {
                "id": article["id"],
                "title": article["title"].strip(),
                "content": article["content"].strip(),
                "source": article["source"].lower(),
                "published_at": article["published_at"],
            }
        )
    return cleaned
