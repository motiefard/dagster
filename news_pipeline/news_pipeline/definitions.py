from dagster import Definitions, load_assets_from_modules

from news_pipeline import assets
from .assets import raw_news_articles, cleaned_news_articles, daily_news_analytics, daily_news_report
from .resources import news_api_resource

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[raw_news_articles, cleaned_news_articles, daily_news_analytics, daily_news_report],
    resources={
        "news_api": news_api_resource,
    },
)
