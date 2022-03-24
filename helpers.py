def get_days_with_more_tweets(df, n):
    top_n_users = df['date'].value_counts()[:n]
    for username, count in zip(top_n_users.index, top_n_users):
        print(f"{(username + ':').ljust(15)}{count}")