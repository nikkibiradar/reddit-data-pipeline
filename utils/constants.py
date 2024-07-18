#import congfigparser and with the parcer, going to mark each of the entires thats in the config.conf into the constants.py

import configparser
import os

parser = configparser.ConfigParser()    #initialization

# specify the source of the of the config file i.e., reddit-data-pipeline
# rn we are inside the constants file, so we get the dirname of the current constants file i.e, utils and join that with config.conf
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

#reddit api access
SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_NAME = parser.get('database', 'database_name')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USERNAME = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')

#AWS s3 access
AWS_ACCESS_KEY_ID = parser.get('aws','aws_access_key_id')
AWS_SECRET_ACCESS_KEY = parser.get('aws','aws_secret_access_key')
AWS_REGION = parser.get('aws','aws_region')
AWS_BUCKET_NAME = parser.get('aws','aws_bucket_name')

INPUT_PATH = parser.get('file_paths','input_path')
OUTPUT_PATH = parser.get('file_paths','output_path')

POST_FIELDS = {
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied',
}