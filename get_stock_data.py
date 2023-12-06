# 필요한 라이브러리를 impor
import matplotlib
import matplotlib.pyplot as plt
# 대화형 모드를 활성화
matplotlib.pyplot.ion()

import pandas as pd
import os
import pandas_datareader as pdr
from pandas.plotting import table

### start here
# 주가 데이터를 가져오고 가공하는 클래스를 정의
class GetStockData:
    def get_stock_data(self,Stock_code, start_date, end_date):
        try:
            self.stock_code = Stock_code
             # NaverFinance에서 주가 데이터를 가져옴
            self.stock_data = pdr.naver.NaverDailyReader(self.stock_code, start_date, end_date).read()
            return self.stock_data
        
        except Exception as e:
            print(f"Error fetching data for {self.stock_code}: {e}")
            return None
        
    def change_stock_data_type(self,stock_data):
        # 'Close' 열의 데이터를 숫자로 변환하고 인덱스를 날짜 형식으로 변환
        self.stock_data['Close'] = pd.to_numeric(stock_data['Close'], errors='coerce')
        self.stock_data['High'] = pd.to_numeric(stock_data['High'], errors='coerce')
        self.stock_data['Low'] = pd.to_numeric(stock_data['Low'], errors='coerce')
        
        self.stock_data.index = pd.to_datetime(stock_data.index)
        self.stock_data = self.stock_data.sort_index()
        return self.stock_data

    # 주가 데이터를 시각화하여 그래프를 저장
    def save_stock_data(self,stock_data, company_name,chart_dir):
        plt.figure(figsize=(10, 4))
        plt.plot(stock_data.index, stock_data['Close'])
        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title(f"Stock Price Trend of {self.stock_code}")

        chart_name = os.path.join(chart_dir, f'{company_name}_chart.png')
        plt.savefig(chart_name)

    def save_stock_data_high(self,stock_data, company_name,chart_dir):
        plt.figure(figsize=(10, 4))
        plt.plot(stock_data.index, stock_data['High'])
        plt.xlabel('Date')
        plt.ylabel('High')

        plt.title(f"Stock High Price Trend of {self.stock_code}")

        chart_name_high= os.path.join(chart_dir, f'{company_name}_high_chart.png')
        plt.savefig(chart_name_high)
        

    def save_stock_data_low(self,stock_data, company_name,chart_dir):
        plt.figure(figsize=(10, 4))
        plt.plot(stock_data.index, stock_data['Low'])
        plt.xlabel('Date')
        plt.ylabel('Low')

        plt.title(f"Stock Low Price Trend of {self.stock_code}")

        chart_name_low = os.path.join(chart_dir, f'{company_name}_low_chart.png')
        plt.savefig(chart_name_low)

    def save_stock_data_gap(self,stock_data, company_name,chart_dir):
        plt.figure(figsize=(10, 4))
        plt.plot(stock_data.index, stock_data['High']-stock_data['Low'])
        plt.xlabel('Date')
        plt.ylabel('Gap')

        plt.title(f"Stock Gap Price Trend of {self.stock_code}")

        chart_name_gap = os.path.join(chart_dir, f'{company_name}_gap_chart.png')
        plt.savefig(chart_name_gap)
    
    # 주가 데이터를 테이블로 표현하여 저장   
    def save_stock_table(self,stock_data, company_name, chart_dir):
        plt.figure(figsize=(15, 4))
        ax = plt.subplot(111, frame_on=False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        # 날짜 기준으로 내림차순으로 정렬하고 상위 10개의 데이터를 표로 나타냄. 
        stock_data_sorted = stock_data.sort_index(ascending=False)
        table(ax, stock_data_sorted.head(10), loc='center', cellLoc='center', rowLoc='center')

        table_name = os.path.join(chart_dir, f'{company_name}_table.png')
        plt.savefig(table_name)


### end here