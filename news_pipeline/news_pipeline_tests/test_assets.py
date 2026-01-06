from dagster import build_op_context
from news_pipeline.assets import cleaned_news_articles

def test_cleaned_news_articles():
    raw_input = [
        {
            "id": 1,
            "title": "  Hello Dagster ",
            "content": " Great tool ",
            "source": "BBC",
            "published_at": "2025-01-01",
        }
    ]

    context = build_op_context(partition_key="2025-01-01")

    result = cleaned_news_articles(context, raw_input)

    assert result[0]["title"] == "Hello Dagster"
    assert result[0]["content"] == "Great tool"
    assert result[0]["source"] == "bbc"


def test_partition_key_used():
    context = build_op_context(partition_key="2025-01-10")

    assert context.partition_key == "2025-01-10"
