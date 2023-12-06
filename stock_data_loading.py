import pandas as pd
import FinanceDataReader as fdr

### start here

class StockDataLoading:
    def load_stock_from_KRX(self):
        self.krx_url = 'https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'
        self.stk_data = pd.read_html(self.krx_url, header=0, encoding='euc-kr')[0]
        self.stk_data = self.stk_data[['회사명', '종목코드']]
        self.stk_data = self.stk_data.rename(columns={'회사명': 'Name', '종목코드': 'Code'})
        self.stk_data['Code'] = self.stk_data['Code'].apply(lambda input: '0' * (6 - len(str(input))) + str(input))
        return self.stk_data

    def load_stock_KRX_fdr(self):
        self.krx_data = fdr.StockListing("KRX")
        self.krx_data = self.krx_data[['Code', 'Name']]
        return self.krx_data

    def get_match_stock_data(self,company_name, stock_data):
        # 대소문자 구분 없이 회사명이 포함되는 행 찾기
        self.match_rows = stock_data[stock_data['Name'].str.lower().str.contains(company_name.lower())]

        if not self.match_rows.empty:
            # 매치된 행이 있다면 해당 종목 코드들과 회사명 반환
            return self.match_rows[['Code', 'Name']].values.tolist()
        else:
            return None  # 일치하는 회사명이 없을 경우 None 반환
        
### end here