# import pandas as pd
## Solution 1
# def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    
#     not_boring = cinema.loc[(cinema['id'] % 2 != 0) & (cinema['description'] != 'boring'), ['id', 'movie', 'description', 'rating']]\
#     .sort_values(by='rating', ascending=False)

#     return not_boring

import pandas as pd

data = {'id': [1, 2, 3, 4, 5],
        'movie': ['War', 'Science', 'Irish', 'Ice Song', 'House Card'],
        'description': ['Great 3D', 'Fiction', 'boring', 'Fantasy', 'Interesting'],
        'rating': [8.9, 8.5, 6.2, 8.6, 9.1]}

cinema = pd.DataFrame(data)

not_boring = cinema.loc[(cinema['id'] % 2) & (cinema['description'] != 'boring'), ['id', 'movie', 'description', 'rating']]
print(not_boring)
