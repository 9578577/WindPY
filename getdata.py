import tushare as ts

df = ts.get_hist_data('000039')
#直接保存
df.to_csv('./000039.csv')

#选择保存
df.to_csv('./000039.csv',columns=['open','high','low','close'])
