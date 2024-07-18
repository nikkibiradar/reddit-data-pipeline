from etls.reddit_etl import connect_reddit, load_data_to_csv
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
from etls.reddit_etl import extract_posts
from etls.reddit_etl import transform_data
import pandas as pd

# sending a particular instance of reddit in this function
def reddit_pipeline(file_name:str, subreddit:str, time_filter='all', max_posts=5000, retries=3, backoff_factor=2):

    #connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #extraction
    posts = extract_posts(instance, subreddit, time_filter, max_posts=max_posts, retries=retries, backoff_factor=backoff_factor)
    post_df = pd.DataFrame(posts)
    
    #transformation
    post_df = transform_data(post_df)
    
    #loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path