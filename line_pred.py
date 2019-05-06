'''
SMA5 5日均线的绘制
'''
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md
import pandas as pd

#转换日期字符串输出格式
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	d=dt.datetime.strptime(dmy, '%d-%m-%Y')
	date = d.date()
	t = date.strftime('%Y-%m-%d')
	return t

#读取文件
dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices = \
		np.loadtxt(
			'/Users/yujzhang/Documents/spider_data/data_set/da_data/aapl.csv',
			delimiter=',', 
			usecols=(1, 3, 4, 5, 6),
			dtype='M8[D], f8, f8, f8, f8',
			unpack=True, 
			converters={1:dmy2ymd})
        
N = 5
pred_prices = np.zeros(closing_prices.size - 2 * N + 1)   
for i in range(pred_prices.size):
    a = np.zeros((N, N))
    for j in range(N):
        a[j,] = closing_prices[i + j:i + j + N]
    b = closing_prices[i + N:i + N * 2]
    x = np.linalg.lstsq(a, b)[0]
    pred_prices[i] = b.dot(x)


#把收盘价绘制到窗口中
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Dates', fontsize=14)
mp.ylabel('Prices', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 设置mp针对日期类型的刻度定位器
ax = mp.gca()
# 每周一为x轴的主刻度
ax.xaxis.set_major_locator(
		md.WeekdayLocator(byweekday=md.MO))
#设置主刻度的格式
ax.xaxis.set_major_formatter(
		md.DateFormatter('%d %b %Y'))

# 次刻度为日刻度定位器 (每天一刻度)
ax.xaxis.set_minor_locator(md.DayLocator())

dates = dates.astype(md.datetime.datetime)
#mp.plot(dates, closing_prices, color='dodgerblue',
#		linestyle=':', linewidth=3, alpha=0.8,
#		label='AAPL')

# 绘制5日均线
sma5 = np.zeros(closing_prices.size - 4)
for i in range(sma5.size):
	sma5[i] = np.mean(closing_prices[i:i+5])
mp.plot(dates[4:], sma5, color='red',
	linewidth=1, label='SMA-5')

# 卷积绘制5日均线
core = np.ones(5) / 5
sma52 = np.convolve(closing_prices, core, 'valid')
mp.plot(dates[4:], sma52, color='orangered',
	linewidth=5, label='SMA-52', alpha=0.4)


dates = np.append(dates, dates[-1] + pd.tseries.offsets.BDay())
mp.plot(dates[2 * N:], pred_prices, 'o-', 
        c = 'orangered', linewidth=3, 
        label='Predicted Price')

mp.gcf().autofmt_xdate()
mp.legend()
mp.show()









