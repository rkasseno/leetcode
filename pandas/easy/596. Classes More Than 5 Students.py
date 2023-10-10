import pandas as pd

# Solution 1
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_count = courses['class'].value_counts().reset_index()
    result = class_count.loc[class_count['count'] >= 5, ['class']]
    return result

# Solution 2
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby('class', as_index=False).count()
    result = grouped.loc[grouped['student'] >= 5, ['class']]
    return result



