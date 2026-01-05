from dagster import ScheduleDefinition, build_schedule_from_partitioned_job
from .jobs import news_pipeline_job
from .assets import (
    raw_news_articles,
    cleaned_news_articles,
    daily_news_analytics,
    daily_news_report,
)

# daily_news_schedule = ScheduleDefinition(
#     name="daily_news_schedule",
#     # cron_schedule="0 0 * * *",  # Every day at midnight (UTC)
#     cron_schedule="*/1 * * * *",  # Every day at midnight (UTC)
#     target=[
#         raw_news_articles,
#         cleaned_news_articles,
#         daily_news_analytics,
#         daily_news_report,
#     ],
#     run_config={
#         "ops": {
#             "raw_news_articles": {
#                 "config": {
#                     "limit": 10
#                 }
#             }
#         }
#     },
# )


daily_news_schedule = build_schedule_from_partitioned_job(
    news_pipeline_job
)
