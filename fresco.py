import pandas as pd
dates = pd.date_range('01-Sep-2017', '15-Sep-2017')
dates[2]
dates_to_be_searched = ['14-Sep-2017', '9-Sep-2017']
df = pd.DataFrame({'Date': dates_to_be_searched})
d1=df['Date'] = pd.to_datetime(df['Date'])
print(d1)
dates.isin(d1)

