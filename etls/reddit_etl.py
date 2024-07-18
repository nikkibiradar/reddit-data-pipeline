import time
from praw import Reddit
import praw
import sys
import pandas as pd
import numpy as np
import prawcore

from utils.constants import POST_FIELDS

# this is for connecting to reddit
# connecting to the reddit instance using praw library
def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,                   # reddit application client ID
                             client_secret=client_secret,           # reddit application secret
                             user_agent=user_agent)                 # a unique identifier that helps reddit determine the source of requests
        print("Connected to reddit!")
        return reddit                                               # returning an instance of reddit connection
    except Exception as e:
        print(e)
        sys.exit(1)

# extracting the reddit posts
def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, max_posts=5000, retries=3, backoff_factor=2):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=None)
    post_lists = []
    count = 0
    attempt = 0

    while attempt < retries:
        try:
            for post in posts:
                post_dic = vars(post)
                post = {key: post_dic[key] for key in POST_FIELDS}     # mapping each of the 'key's in the POST_FIELDS created in constants.py
                post_lists.append(post)
                count += 1
                if count >= max_posts:
                    break
                if count % 100 == 0:
                    time.sleep(2)
            break
        except prawcore.exceptions.ServerError as e:
            attempt += 1
            wait_time = backoff_factor ** attempt
            print(f"Server error, retrying in {wait_time} seconds...")
            time.sleep(wait_time)          
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    
    print(f"Total posts fetched: {count}")
    if attempt == retries:
        print("Max retries reached, failed to fetch posts")
    
    return post_lists

# transforming reddit data thats extracted 
def transform_data(post_df: pd.DataFrame):
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                post_df['edited'], edited_mode).astype(bool)    # if edited has true/false values, replacing it with the edited_mode
    post_df['title'] = post_df['title'].astype(str)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['author'] = post_df['author'].astype(str)
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit = 's')
    
    return post_df

def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)