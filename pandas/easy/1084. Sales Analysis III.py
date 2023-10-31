import pandas as pd

# Runtime: Beats 93.56%
def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(sales, product, on='product_id')
    min_max = merged.groupby(['product_id', 'product_name'], as_index=False)['sale_date'].agg(['min', 'max'])
    result = min_max.loc[(min_max['min'] >= '2019-01-01') & (min_max['max'] <= '2019-03-31'), ['product_id', 'product_name']]
    return result