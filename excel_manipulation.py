import pandas as pd

  
data = pd.read_excel('gpsdata.xlsx')

df=pd.DataFrame(data)
# df1['Speed'] = df['Speed'].str.replace(' km/h', '').astype(float)
# df=pd.to_numeric(['Speed'])

# df['converstion'] = df['Speed'].str.replace(' km/h', '').astype(float)

# df['converstion'] = df['converstion'].replace(' km/h', '').astype(int)
# # df=df.assign(convertion = intt)


# # df.to_csv("trail.csv")
# print(df['Speed'].head())
# # print(type(df['Speed']))
df['Time'] = pd.to_datetime(df['Time'])

df['date'] = df['Time'].dt.date
df['time'] = df['Time'].dt.time
df['day'] = df['Time'].dt.hour
print(df)