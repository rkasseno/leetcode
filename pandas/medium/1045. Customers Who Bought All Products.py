import pandas as pd

# Runtime: Beats 81.47%
def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    customer.drop_duplicates(inplace=True)
    count = 0
    ids = []
    for unique_id in customer['customer_id'].unique():
        for id in customer['customer_id']:
            if unique_id == id:
                count += 1
        if count == len(product):
            ids.append(unique_id)
        count = 0
    result = pd.DataFrame({'customer_id' : ids})

    return result