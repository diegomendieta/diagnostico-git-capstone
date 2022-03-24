# https://stackoverflow.com/questions/2527892/parsing-a-tweet-to-extract-hashtags-into-an-array
def extract_hashtags(s):
    return [part.split('#')[1] for part in s.split() if part.startswith('#')]


def get_most_used_hashtags(df, n):
    content = df['renderedContent']
    hashtags_df = content.apply(extract_hashtags)
    hashtag_count = hashtags_df.explode('renderedContent').value_counts()[:n]
    
    for hashtag, count in zip(hashtag_count.index, hashtag_count):
        print(f"{(hashtag + ':').ljust(30)}{count}")
