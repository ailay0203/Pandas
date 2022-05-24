# df+1
import pandas as pd

df = pd.DataFrame({'name': ['noa', 'ayala', 'tal', 'lea', ],
                   'gender': ['f', 'f', 'm', 'f'],
                   'age': ['18', '19', '23', '30']})

# df2
df2 = df[['name']]

# df3
df3 = df.loc[(df['gender'] == 'f')]

# df4
df4 = df.loc[df['age'] == '19']

# df5
df5 = df.loc[df['name'] != 'tal']

# df6
df6 = df.loc[(df['name'] == 'tal') | (df['age'] < '20')]

df7 = df[(df['gender'] == 'f') & (df['age'] < '20')]

# df8
df8 = df.loc[(df['name'] != 'tal') & (df['age'] < '20')]

# print(df8)
# df9
df9 = df[(df['gender'] == 'f') & (df['age'] < '20')]


# df10
df10 = pd.read_excel("people.xlsx")

# df11
df11 = df10.loc[(df10['age'] == 95)]

# df12
df12 = df10.loc[(df10['name'] == 'Tal')]

# df13
df13 = df10.loc[(df10['name'] == 'Tal')]

# df14
df14 = df10.loc[(df10['age'] == 22)]

# df15
df15 = df10.loc[(df10['name'] == 'Maya') | (df10['name'] == 'Tal')]

# df16
df16 = df10.loc[(df10['name'] == 'Nadav') | (df10['age'] == 6)]

# df17
df17 = df10.loc[(df10['age'] == 21) | (df10['age'] == 23)]

# df18
df18 = df10.loc[(df10['age'] >= 21) & (df10['age'] <= 23)]

# df19
df19 = df10.loc[(df10["name"] != 'noa')]

# df20
df20 = df10.loc[(df10['age'] > 15) & (df10['age'] < 20) & (df10['gender'] == 'F')]

# df21
df21 = df10.loc[(df10['age'] != 35) & (df10['age'] != 30)]

# df22
df22 = df10.loc[(df10['age'] == 21) & (df10['gender'] == 'M')]

# df23
df23 = df10.loc[(df10['name'] == ' Tal') & (df10['gender'] == 'M')]

# df24
df24 = df10.loc[(df10['gender'] == 'F') & (df10['age'] > 6) & (df10['age'] < 20)]

# df25
df25 = df10.loc[(df10['birth_date'].isnull())]

# df26
# df26 = df10.loc[(df10['name'] == 'Tal') |
#                 (df10['name'] == 'Noa') |
#                 (df10['name'] == 'Shlomi') &
#                 (df10['gender'] == ' F') &
#                 (df10['age'] >= 50)]

df26 = df10.loc[(df10['name'].isin(['Tal', 'Noa', 'Shlomi'])) |
                (df10['gender'] == ' F') &
                (df10['age'] >= 50)]
print(df26)
# df27
df27 = df10.loc[(df10['gender'] == 'F') &
                (df10['age'] == 5) &
                (df10['name'] == 'Ido') &
                (df10['gender'] == 'F') & (df10)]
