import pandas as pd
columns = 'region country item_type channel priority order_date, order_id ship_date sold price cost'.split()
df = pd.read_csv('../DATA/sales_records.csv', parse_dates=True, skiprows=1,
                 dtype={'region': 'category', 'country': 'category', 'item_type': 'category', 'channel': 'category', 'sold': 'category'}, names=columns)  # <.>
print(df.describe())  # <.>
print()

print(df.info(memory_usage="deep"))  # <.>
print()

print(df.head(10))  # <.>

print()

print(df.describe(include='O'))
print()

print(df.value_counts('region'))
print()
