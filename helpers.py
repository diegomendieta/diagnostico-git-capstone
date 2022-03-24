def get_most_retweeted(df, n):
    retweet_count_df = df.nlargest(n, 'retweetCount')
    for _, row in retweet_count_df.iterrows():
        print(f"Retweet count: {row['retweetCount']}\n\n{row['renderedContent']}\n")
        print('-------------------\n')