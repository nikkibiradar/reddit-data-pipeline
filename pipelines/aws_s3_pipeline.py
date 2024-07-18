from etls.aws_etl import connect_to_s3, upload_to_s3
from utils.constants import AWS_BUCKET_NAME
from etls.aws_etl import create_bucket_if_not_exists

# ti -> task id 
def upload_s3_pipeline(ti):
    # file name is being fetched from airflow -> XComs
    # when we finish running reddit_pipeline task, we get a return value of the file path, "/opt/airflow/data/output/reddit_20240715.csv"
    # this we can see in the XComs and pull task id and file path from there 
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

    # connnecting to the s3 bucket
    s3 = connect_to_s3()

    # create a bucket if it does not exists
    create_bucket_if_not_exists(s3, AWS_BUCKET_NAME)

    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])   # spiltting it to get file name -> reddit_20240715.csv