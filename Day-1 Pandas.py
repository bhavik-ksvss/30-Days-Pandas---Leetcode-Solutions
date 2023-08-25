#Q1. Big Countries
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_countries=world[(world['area']>=3000000) | (world['population']>=25000000)]
    result=big_countries[["name", "population", "area"]]

    return result

#Q2. Recyclable and Low Fat Products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowfat_recyclable= products[(products['low_fats']=='Y') & (products['recyclable']=='Y')]
    result=lowfat_recyclable[['product_id']]

    return result 

#Q3. Customers Who Never Order
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df=customers.merge(orders,how='left',left_on='id',right_on='customerId')

    mask=merged_df['customerId'].isna()
    print(mask)

    result_df=merged_df[mask]
    print(result_df)

    result_df=result_df[['name']].rename(columns={'name':'Customers'})

    return result_df

#Q4.Article Views I
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    views_df=views[views['author_id']==views['viewer_id']][['author_id']]


    df_alias = views_df.rename(columns={'author_id': 'id'}).sort_values(by='id').drop_duplicates(subset='id')

    # sorted_df = df_alias.sort_values(by='id')

    # distinct_sorted_df = sorted_df.drop_duplicates(subset='id')

    return df_alias