import pandas as pd

# Solution 1
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'].replace({'m' : 'f', 'f' : 'm'}, inplace=True)
    return salary

# Solution 2
def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    for index, row in salary.iterrows():
        if row['sex'] == 'm':
            salary.loc[index, 'sex'] = 'f'
        else:
            salary.loc[index, 'sex'] = 'm'
    return salary
