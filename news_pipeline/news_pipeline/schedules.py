from dagster import ScheduleDefinition

from .assets import (
    raw_news_articles,
    cleaned_news_articles,
    daily_news_analytics,
    daily_news_report,
)

daily_news_schedule = ScheduleDefinition(
    name="daily_news_schedule",
    cron_schedule="0 0 * * *",  # Every day at midnight (UTC)
    target=[
        raw_news_articles,
        cleaned_news_articles,
        daily_news_analytics,
        daily_news_report,
    ],
    run_config={
        "ops": {
            "raw_news_articles": {
                "config": {
                    "limit": 10
                }
            }
        }
    },
)
