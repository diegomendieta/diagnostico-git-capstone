
def get_most_retweeted(df, n):
    retweet_count_df = df.nlargest(n, 'retweetCount')
    for _, row in retweet_count_df.iterrows():
        print(f"Retweet count: {row['retweetCount']}\n\n{row['renderedContent']}\n")
        print('-------------------\n')

def get_users_who_tweet_the_most(df, n):
    top_n_users = df['username'].value_counts()[:n]
    for username, count in zip(top_n_users.index, top_n_users):
        print(f"{(username + ':').ljust(30)}{count}")

