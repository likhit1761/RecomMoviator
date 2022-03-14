import pandas as pd

metapath = 'movies_metadata.csv'
df = pd.read_csv(metapath)
meanvote = df['vote_average'].mean()
minvote = df['vote_count'].mean()
minvote = df['vote_count'].quantile(0.90)
filteredMovies = df.copy().loc[df['vote_count'] >= minvote]


def weightedRating(x, minvote=minvote, meanvote=meanvote):
    voters = x['vote_count']
    avg_vote = x['vote_average']
    return (voters / (voters + minvote) * avg_vote) + (minvote / (minvote + voters) * meanvote)


filteredMovies['score'] = filteredMovies.apply(weightedRating, axis=1)
filteredMovies = filteredMovies.sort_values('score', ascending=False)
pd.set_option('precision', 2)
print(filteredMovies.head(20))
