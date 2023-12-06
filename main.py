
from pandas.plotting import table
import pandas as pd

import schedule
import time
import os
import datetime

### start here

from stock_data_loading import StockDataLoading
from get_stock_data import GetStockData
from make_report import MakeReport
from send_mail import SendMail
      
if __name__ == '__main__':
    # StockDataLoading, GetStockData, MakeReport 클래스의 인스턴스 생성
    load_data = StockDataLoading()
    get_data = GetStockData()
    report = MakeReport()
    
    # KRX(한국거래소)에서 모든 종목의 데이터를 로드
    df_stock = load_data.load_stock_from_KRX()
    df_stock_fdr = load_data.load_stock_KRX_fdr()
 
    # 사용자로부터 입력 받은 회사명(회사명의 일부만 입력 가능)
    user_input = input("원하는 회사명을 입력하세요: ")

    # 입력 받은 회사명이 포함된 모든 회사들의 종목 코드 및 회사명 가져온 후 출력
    stock_info = load_data.get_match_stock_data(user_input, df_stock_fdr)
    if stock_info:
        for code, name in stock_info:
            print(f"{name}: 코드는 {code} 입니다.")
    else:
        print(f"{user_input}과(와) 관련된 종목이 데이터에 없습니다.")  
  
    # 사용자로부터 입력 받은 종목 코드
    stock_code = input("종목 코드를 입력하세요: ")
    for code, name in stock_info:
        if code == stock_code:
            company_name = name
    
    
    # 종목 코드를 이용하여 해당 종목의 일별 주가 데이터를 가져옴
    end_date = datetime.datetime.now().strftime('%Y%m%d')
    stock_data = get_data.get_stock_data(stock_code, '20230130', end_date)

    if stock_data is not None:
        pd.set_option('display.max_rows', None)
        # 주가 데이터를 엑셀 및 CSV 파일로 저장
        stock_data.to_excel(f"{company_name}_daily_data.xlsx")
        stock_data.to_csv(f"{company_name}_daily_data.csv")
        print(stock_data)     
        # 차트를 저장할 디렉토리 생성
        chart_dir = 'C:/Users/stock_report'
        os.makedirs(chart_dir, exist_ok=True)

        # 주가 데이터 전처리
        stock_data = get_data.change_stock_data_type(stock_data)
        
        # 주가 데이터를 시각화하고 차트 저장
        get_data.save_stock_data(stock_data, company_name, chart_dir)
        
        get_data.save_stock_data_high(stock_data, company_name, chart_dir)
        get_data.save_stock_data_low(stock_data, company_name, chart_dir)
        get_data.save_stock_data_gap(stock_data, company_name, chart_dir)


        # 주가 데이터 테이블을 저장
        get_data.save_stock_table(stock_data, company_name, chart_dir)
        
    else:
        print("일별 시세를 가져오지 못했습니다.")
        
    today = datetime.datetime.today().strftime('%Y%m%d')    
    report.add_title(f'[{company_name}] 주식 보고서',f"보고서 작성일 : {today} \n provider: RX2")
    
    
    # 보고서에 차트와 테이블 추가
    report.add_chart1(f"\n[{company_name}]\n{stock_data.iloc[0]['Close']}원에 거래 마감\n<Chart>",
                           os.path.join(chart_dir, f'{company_name}_chart.png'))
    
    report.add_chart2("<High_chart>",os.path.join(chart_dir, f'{company_name}_high_chart.png'))
    
    report.add_chart3("<Low Chart>",os.path.join(chart_dir, f'{company_name}_low_chart.png'))
    
    report.add_chart4("<Gap Chart>",os.path.join(chart_dir, f'{company_name}_gap_chart.png'))
    
    report.add_table_("<Table>",os.path.join(chart_dir, f'{company_name}_table.png'))
    
    # 보고서 저장
    ppt = report.save_report()

    
    # 이메일 전송을 위한 SendMail 인스턴스 생성
    send = SendMail(ppt,today)
    
    # 매일 지정된 시간에 이메일 전송
    schedule.every().day.at("17:55").do(send.send_email)
    while True:
        schedule.run_pending()
        time.sleep(1)

### end here