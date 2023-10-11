import pandas as pd

# Solution 1
# Runtime: Beats 73.18%
# Memory: Beats 73.76%
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    numbers_dict =  {}
    for i in range(len(logs['num'])-2):
        if (logs['num'][i] == logs['num'][i+1]) & (logs['num'][i+1] == logs['num'][i+2]):
            numbers_dict[logs['num'][i]] = logs['num'][i]
        else:
            continue
    result = pd.DataFrame({'ConsecutiveNums' : numbers_dict.keys()})
    return result

# Solution 2
# Runtime: Beats 62.39%
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['std'] = logs['num'].rolling(3).std()
    result = pd.DataFrame({'ConsecutiveNums' : logs.query('std == 0')['num'].unique()})
    return result
