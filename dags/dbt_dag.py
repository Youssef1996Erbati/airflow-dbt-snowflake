from airflow import DAG
from pendulum import datetime

from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

with DAG(
    dag_id="dbt_snowflake_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "snowflake"],
) as dag:

    dbt_tasks = DbtTaskGroup(
        group_id="dbt_run",
        project_config=ProjectConfig(
            dbt_project_path="/opt/airflow/dags/dbt/Project_dbt"
        ),
        profile_config=ProfileConfig(
            profile_name="Project_dbt",
            target_name="dev",
            profile_mapping=SnowflakeUserPasswordProfileMapping(
                conn_id="snowflake_default",
                profile_args={
                    "database": "DBT_DB",
                    "schema": "PUBLIC",
                    "warehouse": "DBT_WH",
                    "role": "ACCOUNTADMIN",
                },
            ),
        ),
        execution_config=ExecutionConfig(
            dbt_executable_path="/home/airflow/.local/bin/dbt",
        ),
    )