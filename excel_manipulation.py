import pandas as pd

  
# data = pd.read_excel('gpsdata.xlsx')

# df=pd.DataFrame(data)
# # df1['Speed'] = df['Speed'].str.replace(' km/h', '').astype(float)
# # df=pd.to_numeric(['Speed'])

# # df['converstion'] = df['Speed'].str.replace(' km/h', '').astype(float)

# # df['converstion'] = df['converstion'].replace(' km/h', '').astype(int)
# # # df=df.assign(convertion = intt)


# # # df.to_csv("trail.csv")
# # print(df['Speed'].head())
# # # print(type(df['Speed']))
# df['Time'] = pd.to_datetime(df['Time'])

# df['date'] = df['Time'].dt.date
# df['time'] = df['Time'].dt.time
# df['day'] = df['Time'].dt.hour
# print(df)
# import pandas as pd

# df = pd.read_csv('trail.csv')

# print(df.to_string()) 

# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# c = {
#     1:"a",
#     2:'b'
# }
# myvar = pd.DataFrame(mydataset)

# print(myvar)
# a=pd.DataFrame(c)
# print(a)

# print(pd.__version__)
# c=[1, 2, 3, 4]
# print(pd.Series(c))

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df.loc[[0, 2]])
# print(pd.options.display.max_rows)

# df=pd.read_csv('trail.csv')
# print(pd.max_rows)
# print(df.describe())

df = pd.read_excel("mccs - 2_Vth sem.xlsx")
new_df = df.dropna()
print(new_df.head())