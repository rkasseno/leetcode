import pandas as pd

# Solution 1
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(subset='salary', inplace=True)
    result = pd.DataFrame({'SecondHighestSalary' : [employee['salary'].nlargest(2).iloc[-1]]}) if len(employee) >= 2\
    else pd.DataFrame({'SecondHighestSalary' : [None]})
    
    return result

# Solution 2
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    if (len(employee) <= 1) | (len(employee['salary'].unique()) == 1):
        return pd.DataFrame({'SecondHighestSalary' : [None]})

    employee.sort_values(by='salary', ascending=False, inplace=True, ignore_index=True)

    for i in range(len(employee['salary'])-1):
        if employee['salary'][i] > employee['salary'][i+1]:
            result = pd.DataFrame({'SecondHighestSalary' : [employee['salary'][i+1]]})
            break
        else:
            continue
    
    return result
