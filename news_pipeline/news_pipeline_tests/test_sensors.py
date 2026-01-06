from dagster import SensorEvaluationContext, build_op_context
from news_pipeline.sensors import new_articles_sensor
from news_pipeline.jobs import news_pipeline_job

# def test_sensor_triggers_run():
#     context = SensorEvaluationContext(cursor="0")

#     result = list(new_articles_sensor(context))

#     assert len(result) == 1
#     assert result[0].run_key.startswith("new_articles_")


# def test_sensor_no_trigger():
#     context = SensorEvaluationContext(cursor="1000")

#     result = list(new_articles_sensor(context))

#     assert result == []



# def test_job_definition():
#     assert news_pipeline_job.name == "news_pipeline_job"
