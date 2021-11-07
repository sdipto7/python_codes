import pandas as pd
import numpy as np
import csv

# animals = (['Tiger', 'Lion', 'Elephant'])
# animals = pd.Series(animals)
# print(animals)
#
# numbers = pd.Series([64,69,74,79])
# print(numbers)
#
# if np.nan == np.nan:
#     print("Yes")
# else:
#     print("NO")
# print(np.isnan(np.nan))

# animals = pd.Series(['tiger', 'lion', "None"])
# print(animals)
#
# numbers = pd.Series([67,69,66,None])
# print(numbers)

# sports = {'Archery' : 'Bhutan',
#           'Golf' : 'Scotland',
#           'Sumo' : 'Japan',
#           'Taekwondo' : 'South Korea'}
# sports = pd.Series(sports)
# print(sports,'\n')
# print(sports.index, '\n')

# animals = pd.Series(['Tiger', 'Bear', 'Moose'], index = ['Bangladesh', 'America', 'Canada'])
# print(animals, '\n')
#
# sports = {'Archery' : 'Bhutan',
#           'Golf' : 'Scotland',
#           'Sumo' : 'Japan',
#           'Taekwondo' : 'South Korea'}
# sports = pd.Series(sports, index=['Golf', 'Hockey'])
# print(sports)
#
# sports1 = {'Archery' : 'Bhutan',
#            'Hadudu' : 'Bangladesh'}
# sports1 = pd.Series(sports1, index=['Archery', 'Football'])
#
# # sports2 = pd.Series(['Bhutan', 'Bangladesh'], index=['Archery' , 'Hadudu'])
#
# print(sports1, "\n")
# # print(sports2, "\n")


# sports = {'Archery' : 'Bhutan',
#           'Football' : 'England',
#           'Kabadi' : 'Bangladesh',
#           'Cricket' : 'England'}
# sports = pd.Series(sports)
# print(sports['Kabadi'])

# s = {97: 'a',
#      98: 'b',
#      99: 'c',
#      100: 'd'}
# s = pd.Series(s)
# print(s.iloc[0])

# x = pd.Series([100.10,120.13,101.11,3.15])
# total = 0
# for item in x:
#     total+=item
# print(total)
#
# np_total = np.sum(x)
# print(np_total)
# x+=2
# print(x)
# print(np.sum(x))

# s1 = pd.Series({'Football': 'England',
#                 'Kabadi': 'Bangladesh'})
# s2 = pd.Series({'Archery': 'Bhutan',
#                 'Golf': 'Scotland'})
# s3 = s1.append(s2)
#
# print(s1, '\n')
# print(s2, '\n')
# print(s3, '\n')
# print(s3.iloc[3])
# print(s3.loc['Kabadi'])

# s = pd.Series([1,2,3])
# s.iloc[1] = s.iloc[1]**3
# s.loc['Animal'] = 'Bear'
# print(s)

'''
Dataframe
'''

# purchase_1 = pd.Series({'Name': 'Chris',
#                         'Item Purchased': 'Dog Food',
#                         'Cost': 22.50})
# purchase_2 = pd.Series({'Name': 'Kevyn',
#                         'Item Purchased': 'Kitty Litter',
#                         'Cost': 2.50})
# purchase_3 = pd.Series({'Name': 'Vinod',
#                         'Item Purchased': 'Bird Seed',
#                         'Cost': 5.00})
#
# df = pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['Store 1','Store 2','Store 3'])
# print(df)
# print(df.T)
# print(df.loc['Store 2'])
# print(df['Cost'])
# print(type(df.loc['Store 2']))
# print(df.loc['Store 1'])


# print(df.loc['Store 1' , 'Cost'])
# print(df.loc['Store 1']['Cost'])
# print(df['Cost','Store 1'])
# print(df['Cost']['Store 1'])

# print(df.T.loc['Cost'])
# print(df.T.loc['Cost' , 'Store 1'])
# print(df.T.loc['Cost'] ['Store 1'])

# print(df.loc['Store 1',['Name', 'Cost']])
# print(df.loc[['Store 1','Store 3'],['Name', 'Cost']])
# print(df.loc[:,['Name', 'Cost']])

# d = df.drop('Store 2')
# print(d)
# print(df)
# copy_df = df.copy();
# copy_df = copy_df.drop('Store 2')
# # print(copy_df, '\n')
# # print(df)
# del copy_df['Name']
# print(copy_df)

# df['Location'] = None
# # print(df)
# df.loc[:,'Location'] = 'Dhanmondi'
# df.loc[['Store 1','Store 3'],'Location'] = "Gulshan"
# # print(df)

# print(df['Cost'])
# print(df.loc[:,'Cost'])


'''
CSV FILES
'''

df = pd.read_csv('olympics.csv',index_col=0, skiprows=1)
# print(df.head())
# print(df.columns)
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)

# print(df.head(), '\n')

# print(df['Gold'] > 0)

# only_gold = df.where(df['Gold']>0)
# print(only_gold['Gold'].count())
# print(df['Gold'].count())

# print(df[(df['Gold.1'] > 0) & (df['Gold'] == 0)])
# df = df.drop('Totals')
# print(df['Gold'].idxmax())
# print(df['Gold'].max())

# print(abs(df['Gold'] - df['Gold.1']).idxmax())

# print(df)

# for index, col in df.iterrows():
    # points = pd.Series(df['Gold.2'].head())
    # print(points.head())
    # break
    # print(df['Gold.2'].head())
    # break


s1 = df['Gold.2']
s2 = df['Silver.2']
s3 = df['Bronze.2']
points = s1.copy()
i = 0
while i < len(s1):
    points.iloc[i] = s1.iloc[i] * 3
    points.iloc[i] = points.iloc[i] + s2.iloc[i] * 2
    points.iloc[i] = points.iloc[i] + s3.iloc[i]
    i = i + 1

print(points)

# print(s1.head())
# p1 = {"a" : 11,
#       "b" : 12,
#       "c" : 13}
# s = pd.Series(p1)
# print(s)
# print(s.iloc[0])
# i = 0
# while i < len(s):
#     s.iloc[i] = s.iloc[i] * 3
#     print(s.iloc[i])
#     i+=1
