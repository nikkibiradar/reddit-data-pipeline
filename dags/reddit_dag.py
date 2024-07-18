from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
import os
import sys

# if you're running airflow on your docker instance & when you start your DAG and you dont have an insertion into your root directory to reflect
# the root directory, you'll get an error
# fetching root directory name: (reddit-data-pipeline)<-(dags)<-(reddit_dag.py) 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline
from pipelines.aws_s3_pipeline import upload_s3_pipeline

default_args = {
    'owner': 'Nikhita Biradar',
    'start_date': datetime(2024, 7, 13)
}

# format that we are appending our files with; Appending the date to filenames to ensure uniqueness and to keep track of when files were created or modified.
file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False,
    tags = ['reddit', 'etl', 'pipeline']
)

# defining the ETL tasks:

# extraction from reddit
extract = PythonOperator(
    task_id = 'reddit_extraction',
    python_callable = reddit_pipeline,              # "reddit_pipeline" is python function that should be called when this task is executed
    op_kwargs = {                                   # a dictionary of keyword arguments that will be passed to the "reddit_pipeline" python_callable function.
        'file_name' : f'reddit_{file_postfix}',     # the keys and values in this dictionary correspond to the parameters that the "reddit_pipeline" function expects.
        'subreddit': 'memes',
        'time_filter': 'all',
        'max_posts': 5000,              # Increased the number of posts to fetch
        'retries': 3,                   # Added retries parameter
        'backoff_factor': 2             # Added backoff factor parameter
    },
    dag=dag
)

# upload transformed data to aws s3
upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3