from dagster import sensor, RunRequest
from .resources import NewsAPIClient
from .jobs import news_pipeline_job

@sensor(
    job=news_pipeline_job,
    minimum_interval_seconds=30,  # check every 30 seconds
)
def new_articles_sensor(context):
    """
    triggers a pipeline run when new articles appear.
    """

    # api
    api_client = NewsAPIClient(default_limit=100)
    articles = api_client.fetch_articles()

    current_count = len(articles)

    # read last known count
    last_count = int(context.cursor) if context.cursor else 0

    if current_count > last_count:
        # Update cursor (memory)
        context.update_cursor(str(current_count))

        # trigger
        yield RunRequest(
            run_key=f"new_articles_{current_count}",
            run_config={
                "ops": {
                    "raw_news_articles": {
                        "config": {
                            "limit": current_count
                        }
                    }
                }
            },
        )
    else:
        # No new data → do nothing
        return
