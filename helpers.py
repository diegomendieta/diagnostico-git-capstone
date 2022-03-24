def get_users_who_tweet_the_most(df, n):
    top_n_users = df['username'].value_counts()[:n]
    for username, count in zip(top_n_users.index, top_n_users):
        print(f"{(username + ':').ljust(30)}{count}")