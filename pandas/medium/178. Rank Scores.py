import pandas as pd

# Solution 1
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by='score', ascending=False, inplace=True)
    scores['rank'] = scores.groupby('score').ngroup(ascending=False).apply(lambda x: x+1)
    return(scores[['score', 'rank']])

# Solution 2
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by='score', ascending=False, inplace=True)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return(scores[['score', 'rank']])
