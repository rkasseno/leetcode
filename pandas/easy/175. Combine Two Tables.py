
# Runtime: Beats 92.72%
# Memory: Beats 32.74%

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = person.merge(address, on='personId', how='left').reindex(columns=['firstName', 'lastName', 'city', 'state'])
    return merged