# import pandas as pd

# # Memory: Beats 91.18%
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    if (len(employee) == 0) or (len(department) == 0):
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner').rename(columns={'name_x':'Employee', 'name_y':'Department', 'salary': 'Salary'})
    
    grouped = merged.groupby('Department', as_index=False)['Salary'].max()

    result = pd.DataFrame()
    for department, salary in zip(grouped['Department'], grouped['Salary']):
        to_concat = merged.loc[(merged['Department'] == department) & (merged['Salary'] == salary), ['Department', 'Employee', 'Salary']]
        result = pd.concat([result, to_concat])

    return result

# Solution 2
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    if (len(employee) == 0) or (len(department) == 0):
        return pd.DataFrame(columns=['Department', 'Employee', 'Salary'])

    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')\
    .rename(columns={'name_x':'Employee', 'name_y':'Department', 'salary': 'Salary'})
    grouped = merged.groupby('Department', as_index=False)['Salary'].nlargest(1)
    result = pd.merge(grouped, merged, on=['Department', 'Salary'], how='inner')

    return result[['Department', 'Employee', 'Salary']]


