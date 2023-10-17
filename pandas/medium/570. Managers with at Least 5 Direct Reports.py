import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    if len(employee) <= 1:
        data = {'name' : []}
        return pd.DataFrame(data)

    grouped = employee.groupby(['managerId'])['name'].count()

    result = pd.DataFrame()
    for id, count in zip(grouped.index, grouped):
        if count >= 5:
            to_concat = pd.DataFrame({'name' : employee[employee['id'] == id]['name']})
            result = pd.concat([result, to_concat])

    if result.empty:
        data = {'name' : []}
        return pd.DataFrame(data)
    return result
