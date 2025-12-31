from dagster import Definitions, load_assets_from_modules

from news_pipeline import assets
from .assets import raw_news_articles
from .resources import news_api_resource

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=[raw_news_articles],
    resources={
        "news_api": news_api_resource,
    },
)
