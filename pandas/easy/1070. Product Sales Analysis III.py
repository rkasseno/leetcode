import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    first_year = sales.groupby('product_id', as_index=False)['year'].min()
    merged = pd.merge(first_year, sales, on=['product_id', 'year'])
    result = merged.loc[:, ['product_id', 'year', 'quantity', 'price']]
    result.rename(columns={'year' : 'first_year'}, inplace=True)
    return result
