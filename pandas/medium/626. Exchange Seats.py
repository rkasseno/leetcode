import pandas as pd

# Runtime: Beats 84.66%
def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    for i in range(0, len(seat['student'])-1, 2):
        student = seat['student'][i]
        seat.loc[i, 'student'] = seat['student'][i+1]
        seat.loc[i+1, 'student'] = student
    return seat