import pandas as pd

# Best solution
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    result = weather.loc[(weather['recordDate'].diff().dt.days == 1) & (weather['temperature'].diff() > 0), ['id']]
    return result

# Alternative solution
def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True, ignore_index=True)

    array = []

    if len(weather) == 1:
        return pd.DataFrame({'id' : array})

    for index in range(len(weather['recordDate'])-1):
        if (weather['recordDate'][index+1] - weather['recordDate'][index]).days != 1:
            continue
        elif weather['temperature'][index] < weather['temperature'][index+1]:
            array.append(weather.loc[index+1, 'id'])
                
    return pd.DataFrame({'id' : array})