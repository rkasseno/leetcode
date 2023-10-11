import pandas as pd

# Solution 1
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset='salary', inplace=True)
    
    if N > len(employee):
        result = pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    elif len(employee) >= 1:
        result = pd.DataFrame({f'getNthHighestSalary({N})' : [employee['salary'].nlargest(N).iloc[-1]]})
    else:
        result = pd.DataFrame({f'getNthHighestSalary({N})' : [None]})

    return result

# Solution 2
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset='salary', inplace=True)
    
    Nth = f'getNthHighestSalary({N})'
    
    if N > len(employee):
        result = pd.DataFrame({Nth : [None]})
    elif len(employee) >= 1:
        result = pd.DataFrame({Nth : [employee['salary'].nlargest(N).iloc[-1]]})
    else:
        result = pd.DataFrame({Nth : [None]})
