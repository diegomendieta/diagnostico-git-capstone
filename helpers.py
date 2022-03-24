def get_days_with_more_tweets(df, n):
    top_n_users = df['date'].value_counts()[:n]
    for username, count in zip(top_n_users.index, top_n_users):
        print(f"{(username + ':').ljust(15)}{count}")


# https://stackoverflow.com/questions/2527892/parsing-a-tweet-to-extract-hashtags-into-an-array
def extract_hashtags(s):
    return [part.split('#')[1] for part in s.split() if part.startswith('#')]


def get_most_used_hashtags(df, n):
    content = df['renderedContent']
    hashtags_df = content.apply(extract_hashtags)
    hashtag_count = hashtags_df.explode('renderedContent').value_counts()[:n]
    
    for hashtag, count in zip(hashtag_count.index, hashtag_count):
        print(f"{(hashtag + ':').ljust(30)}{count}")


def get_most_retweeted(df, n):
    retweet_count_df = df.nlargest(n, 'retweetCount')
    for _, row in retweet_count_df.iterrows():
        print(f"Retweet count: {row['retweetCount']}\n\n{row['renderedContent']}\n")
        print('-------------------\n')

        
def get_users_who_tweet_the_most(df, n):
    top_n_users = df['username'].value_counts()[:n]
    for username, count in zip(top_n_users.index, top_n_users):
        print(f"{(username + ':').ljust(30)}{count}")
