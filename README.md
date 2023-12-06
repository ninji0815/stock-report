# Automated Daily Stock Analysis System

일별 주식 분석 자동화 시스템
<br/><br/>
## 목차
- [🖥️ 프로젝트 소개](#프로젝트-소개)
  * [🕰️ 개발 기간](#1-개발-기간)
  * [👩‍🤝‍👩 팀원 구성](#2-팀원-구성)
- [⚙️ 필수 패키지(오픈소스 포함)](#필수-패키지오픈소스-포함)
- [🔎 프로젝트의 주요 특징](#프로젝트의-주요-특징)
- [📌 시나리오 및 요구사항](#시나리오-및-요구사항)
- [🧩 Block Diagram](#block-diagram)
- [🔗 UML Sequence Diagram](#uml-sequence-diagram)
- [📂 UML Class Diagram](#uml-class-diagram)
- [📜 파일별 구현 형태](#파일별-구현-형태)
<br/><br/>
## 프로젝트 소개
사용자가 원하는 회사의 주식 정보를 메일로 받아볼 수 있는 자동화 시스템입니다.

주식 열풍이 부는 요즘, 바쁜 현대인들을 위해 고안하였습니다.

 - 효율적인 데이터 수집 및 분석 가능
 - 자동 보고 및 시각화 기능으로 편리하게 시장 동향 파악 가능

 ### 1) 개발 기간
23.11.14 ~ 23.12.06

 ### 2) 팀원 구성
• 팀장 : 이지혜 - (step 4) 보고서 이메일 전송 함수, 클래스와 main 함수의 코드 구현, UML Class Diagram, UML Sequence Diagram

• 팀원1 : 백민지 - (step 1-2) 주식 크롤링 함수, 주식 분석자료 제작 함수, GitHub 작성, UML Class Diagram, UML Sequence Diagram

• 팀원2 : 유원아 - (step 3) 주식 보고서 작성 함수, 프로젝트 시나리오 작성, 최종 발표자료 피피티 및 대본 제작, UML Sequence Diagram

• 팀원3 : 변지연 - (step 2) 주식 분석자료 제작 함수, 중간발표 PPT 제작, 최종 발표자료(Block Diagram) 작성, UML Sequence Diagram
<br/><br/>
## 필수 패키지(오픈소스 포함)
- Ubuntu 20.04에 패키지 설치 방법:

```
sudo pip install pandas
sudo pip install finance-datareader
sudo pip install pandas_datareader
sudo pip install matplotlib
sudo pip install openpyxl
sudo pip install plotly

pip install html5lib
pip install requests
```
```
sudo pip install python-pptx
```
```
sudo pip install schedule
```
1. **pandas**:

   - 표 형태의 데이터를 다루고 다양한 데이터 분석 작업을 수행하는 데 사용.

2. **finance-datareader** (또는 **FinanceDataReader**):

   - 금융 시장 데이터를 가져와서 분석 및 시각화에 사용

3. **pandas_datareader**:

   - 주가, 환율, 경제 지표 등의 금융 데이터를 가져오는 데 사용

4. **matplotlib**:

   - 선 그래프, 막대 그래프, 히스토그램 등을 생성하여 데이터를 시각적으로 표현하는 데 사용

5. **openpyxl**:

   - Excel 파일을 생성, 편집하거나 읽어오는 데 사용

6. **html5lib**:
   
   - 웹 스크레이핑 및 HTML 문서 처리에 사용

7. **requests**:
   
   - 웹 페이지에서 데이터를 가져오거나 API에 요청을 보내는 데 사용

8. **python-pptx**:

   -  파워포인트 프레젠테이션을 동적으로 생성하는 데 사용

9. **schedule**:

   - 주기적으로 실행되어야 하는 작업, 예를 들어 자동화된 스크립트나 백그라운드 작업 등을 처리하는 데 사용
<br/><br/>
## 프로젝트의 주요 특징
 ### 1) 오픈 소스 활용:
- FinanceDataReader
- matplotlib
- Pandas
- datetime
- os
- pptx
- smtplib
- email
- schedule
- time

 ### 2) 강의에서 배운 툴 사용:

   ① library: matplotlib /Pandas excel&csv 파일 저장 응용

   ② tool: jupyter notebook/ GitHub

 ### 3) 자체 개발:

   ① 여러명한테 동시에 email 전송하는 기능

   ② 사용자가 원하는 특정 회시만 볼 수 있도록 입력 받고 크롤링 해오는 기능

   ③ 코드명을 입력하면 일별시세 보여주는 기능

   ④ 정해진 시간에 일별 주식 분석 자료 전송하는 기능
<br/><br/>
## 시나리오 및 요구사항
  ### - step 1. 종목 코드 및 일별 시세 불러오기: 
  - 사용자가 종목코드를 검색하기 위해 프로그램에 회사명을 입력
  - FinanceDataReader를 사용하여 KRX(한국 주식거래소)에서 종목 코드 및 회사명 데이터를 가져옴
  - 사용자가 입력한 회사명이 포함된 회사들을 찾아 종목코드 및 회사명 데이터를 모두 출력
  - 사용자는 원하는 종목 코드를 선택하여 해당 종목의 일별 주식 시세를 가져옴

  ### - step 2. 주식 분석 자료(그래프, 테이블) 준비하기:
  - 가져온 주가 데이터를 Excel(.xlsx)과 Csv(.csv)파일로 저장
  - 차트 저장 디렉토리를 res/stock_report로 설정
  - preprocess_stock_data 함수를 호출하여 주가 데이터를 전처리 함
  - plot_stock_data 함수를 호출하여 전처리된 주가 데이터의 그래프를 생성
  - plot_stock_table 함수를 호출하여 전처리 된 주가 데이터의 상위 10개 항목의 테이블을 생성
  - 생성된 그래프와 테이블을 res/stock_report 디렉토리에 이미지 파일로 저장

  ### - step 3. 보고서 작성하기
  - ppt 객체를 선언하고, 디렉토리에 저장된 파일을 받아옴
  - 파일을 이용하여 보고서 작성
  - 보고서의 첫번째 페이지에 제목 및 부제목(작성 날짜 포함)을 작성
  - 두번째 페이지에는 회사 이름과 거래 마감된 값을 제목으로 작성, 차트와 테이블 작성
  - 최종적으로 작성된 보고서를 ppt형식으로 저장

  ### - step 4. 보고서 이메일 전송하기
  - 송신자의 이메일 주소와 비밀번호를 입력
  - 매일 지정된 시간에 주식 보고서가 첨부된 이메일을 수신자들에게 전송
  - SMTP서버를 통해 전송되며, 송신자의 이메일 주소와 비밀번호를 입력해야 함
  - 이메일은 여러명에게 동시에 전송될 수 있음
  - 메일이 전송되었을 경우에는 성공 메시지가, 실패하였을 경우에는 오류 메시지가 출력됨 
<br/><br/>
## Block Diagram
![image](https://github.com/ninji0815/stock-report/assets/150305171/0ec058eb-8edf-499e-9a35-429d9666c316)

<br/><br/>
## UML Sequence Diagram
### # step 1 ~ step 2
![image](https://github.com/ninji0815/stock-report/assets/150305171/feeb8a07-eb04-4382-a3f1-6bfab814edf0)
---
### # step 3
![image](https://github.com/ninji0815/stock-report/assets/150305171/cfc808ec-0148-4670-9010-e4469c6718a6)
---
### # step 4
![image](https://github.com/ninji0815/stock-report/assets/150305171/f0632df2-0f38-49e8-a429-7538c7e3bc71)
<br/><br/>
## UML Class Diagram
앞선 4단계를 토대로 각각 클래스를 구현 

- 첫 번째, 주식 데이터를 크롤링 후 저장

- 두 번째, 데이터를 토대로 그래프 및 테이블을 작성

- 세 번째, 작성한 그래프, 테이블로 PPT 보고서를 제작 

- 마지막, Sender가 Receiver들에게 SendMail 클래스를 통하여 이메일을 전송

![image](https://github.com/ninji0815/stock-report/assets/150305171/b649b61f-435a-4290-8a2d-9f64d9787f65)
<br/><br/>
## 파일별 구현 형태


|py 파일명|개발 방식|개발 담당 팀원명|
|------|---|---|
|main.py|혼합|이지혜 백민지|
|get_stock_data.py|혼합|변지연 백민지|
|stock_data_loading.py|혼합|백민지|
|make_report.py|Open Source|유원아|
|send_mail.py|혼합|이지혜|
|sender.py|자체개발|이지혜|
|receiver.py|자체개발|이지혜|


<br/><br/>
## 참고문헌
**Journal Articles**

1) Pandas Development Team. (2023). Pandas. [https://pandas.pydata.org/](https://pandas.pydata.org/)

2) Choi, Y. (2018). FinanceDataReader on GitHub. [https://github.com/FinanceData/FinanceDataReader](https://github.com/FinanceData/FinanceDataReader)

**Books**

3) Matplotlib Development Team. (n.d.). Matplotlib Documentation. [https://matplotlib.org/](https://matplotlib.org/)

**Websites**

4) Python Software Foundation. (n.d.). smtplib - SMTP protocol client. [https://docs.python.org/3/library/smtplib.html](https://docs.python.org/3/library/smtplib.html)

5) Python Software Foundation. (n.d.). smtplib.py on GitHub. [https://github.com/python/cpython/blob/main/Lib/smtplib.py](https://github.com/python/cpython/blob/main/Lib/smtplib.py)

6) Python-PPTX Team. (n.d.). python-pptx Documentation. [https://python-pptx.readthedocs.io/](https://python-pptx.readthedocs.io/)

7) Python-PPTX Team. (n.d.). Quickstart Guide. [https://python-pptx.readthedocs.io/en/latest/user/intro.html](https://python-pptx.readthedocs.io/en/latest/user/intro.html)

8) Python Software Foundation. (n.d.). Email Examples. [https://docs.python.org/3/library/email.examples.html](https://docs.python.org/3/library/email.examples.html)

9) Python Software Foundation. (n.d.). datetime — Basic date and time types. [https://docs.python.org/3/library/datetime.html](https://docs.python.org/3/library/datetime.html)

10) Python Software Foundation. (n.d.). os — Miscellaneous operating system interfaces. [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

**Other Sources**

11) JackerLab. (n.d.). Python Library Schedule. [https://schedule.readthedocs.io/](https://schedule.readthedocs.io/)

12) pykrx. (2023). sharebook-kr. [https://github.com/sharebook-kr/pykrx](https://github.com/sharebook-kr/pykrx)


