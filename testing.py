import pandas as pd
s = pd.Series(list('abc'))
print(type(s))
# print('s:\n', s)
print('isin: \n', s[s.isin(['a'])])
data = pd.read_csv('50_states.csv')
print(type(data))
data_series = data['state']
print(type(data_series))
print(data_series[data_series.isin(['Washngton'])].empty)
# print(data.state.isin(['Washington']).empty)

print('s.isin: ', s[s.isin(['bo'])].empty)


# print(s[s.isin(['y'])].empty)
