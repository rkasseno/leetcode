import pandas as pd

# Solution 1
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    unique_count = my_numbers.value_counts().reset_index().sort_values(by=['count', 'num'], ascending=[True, False])
    unique_count = unique_count.loc[unique_count['count'].isin([1]), 'num'].to_frame()
    if unique_count.empty:
        unique_count = pd.DataFrame({'num' : [None]})
        return unique_count
    return unique_count.iloc[:1]

# Solution 2
def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    number_count = my_numbers.value_counts().reset_index()
    result = number_count.loc[number_count['count'] == 1, ['num']].nlargest(columns='num', n=1)
    if result.empty:
        result = pd.DataFrame({'num' : [None]})
    return result

