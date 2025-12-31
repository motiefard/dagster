from dagster import asset, MetadataValue
from datetime import datetime
from collections import Counter

@asset(
    description="raw news articles fetched from the News API",
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
def cleaned_news_articles(context, raw_news_articles):
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
    
    context.add_output_metedata(
        {
            "clean_article_count": len(cleaned),
            "sources": list({a["source"] for a in cleaned}),
        }
    )
    return cleaned


@asset(
    description="analise data",
)
def daily_news_analytics(context, cleaned_news_articles):
    """calc high-level analytics"""
    total_articles = len(cleaned_news_articles)

    #count articles:
    articles_per_source = Counter(
        article['source'] for article in cleaned_news_articles
    )

    # count most common words in titles
    word_counter = Counter()

    for article in cleaned_news_articles:
        words = article["title"].lower().split()
        word_counter.update(words)

    top_words = word_counter.most_common(5)

    res_analytics = {
        "total_articles": total_articles,
        "articles_per_source": dict(articles_per_source),
        "top_title_words": top_words,
    }

    context.add_output_metadata(
        {
            "total_articles": total_articles,
            "sources": list(articles_per_source.keys()),
            "top_word": top_words[0][0] if top_words else "N/A",
        }
    )

    return res_analytics

