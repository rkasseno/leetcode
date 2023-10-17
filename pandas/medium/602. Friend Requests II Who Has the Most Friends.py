import pandas as pd

# Runtime: Beats 68.58%
def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    if len(request_accepted) <= 1:
        empty = {'id' : [None]}
        return pd.DataFrame(empty)

    a = request_accepted.groupby('requester_id', as_index=False)['accepter_id'].count().rename(columns={'requester_id':'id', 'accepter_id':'num'})
    b = request_accepted.groupby('accepter_id', as_index=False)['requester_id'].count().rename(columns={'accepter_id':'id', 'requester_id':'num'})
    concatenated = pd.concat([a, b])
    result = concatenated.groupby('id', as_index=False)['num'].sum().nlargest(1, 'num')

    return result