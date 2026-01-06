from news_pipeline.resources import NewsAPIClient
from dagster import build_op_context
from news_pipeline.assets import raw_news_articles


def test_news_api_client_fetch():
    client = NewsAPIClient(default_limit=3)

    articles = client.fetch_articles(limit=3)

    assert len(articles) == 3
    assert "title" in articles[0]
    assert "source" in articles[0]




def test_raw_news_articles():
    context = build_op_context(
        resources={"news_api": NewsAPIClient(default_limit=3)},
        partition_key="2025-01-01",
        op_config={"limit": 2},
    )

    result = raw_news_articles(context)

    assert len(result) == 2
