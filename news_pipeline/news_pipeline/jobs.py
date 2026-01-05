from dagster import define_asset_job
from .assets import daily_partitions

# This job will materialize ALL assets in the project
news_pipeline_job = define_asset_job(
    name="news_pipeline_job",
    partitions_def=daily_partitions,
)
