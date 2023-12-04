# StockData Report-Project

일별 주식 분석 자동화 시스템

## 목차
  * [🖥️ 프로젝트 소개](#-----------)
  * [👍 프로젝트의 주요 특징](#--------------)
  * [📌 시나리오 및 요구사항](#--------------)
  * [🧩 Block Diagram](#---block-diagram)
  * [🔗 UML Sequence Diagram](#---uml-sequence-diagram)
  * [📂 UML Class Diagram](#---uml-class-diagram)
  * [📄 파일별 구현 형태](#------------)


## 🖥️ 프로젝트 소개
사용자가 원하는 회사의 주식 정보를 메일로 받아볼 수 있는 자동화 시스템입니다.

주식 열풍이 부는 요즘, 바쁜 현대인들을 위해 고안하였습니다.

 - 효율적인 데이터 수집 및 분석 가능
 - 자동 보고 및 시각화 기능으로 편리하게 시장 동향 파악 가능

### 🕰️ 개발 기간
23.11.14 ~ 23.12.06

### 👩‍🤝‍👩 팀원 구성
• 팀장 : 이지혜 - (step 4) 보고서 이메일 전송 단계, 단계별 클래스의 전반적인 코드 구현

• 팀원1 : 백민지 - (step 1-2) 일별 시세 크롤링 및 주식 분석 자료 제작 단계, GitHub 작성

• 팀원2 : 유원아 - (step 3) 주식 보고서 작성 단계, 중간 및 최종 발표자료 피피티 제작

• 팀원3 : 변지연 - (step 2) 주식 분석 자료 제작, 중간 발표자료 제작, 최종 발표자료 내용 구성

### ⚙️ 개발 환경

## 👍 프로젝트의 주요 특징
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
   
## 📌 시나리오 및 요구사항
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

## 🧩 Block Diagram
![image](https://github.com/ninji0815/stock-report/assets/150305171/0ec058eb-8edf-499e-9a35-429d9666c316)

## 🔗 UML Sequence Diagram
### # step 1 ~ step 2
![image](https://github.com/ninji0815/stock-report/assets/150305171/feeb8a07-eb04-4382-a3f1-6bfab814edf0)
---
### # step 3
![image](https://github.com/ninji0815/stock-report/assets/150305171/cfc808ec-0148-4670-9010-e4469c6718a6)
---
### # step 4
![image](https://github.com/ninji0815/stock-report/assets/150305171/f0632df2-0f38-49e8-a429-7538c7e3bc71)

## 📂 UML Class Diagram
앞선 4단계를 토대로 각각 클래스를 구현 

- 첫 번째, 주식 데이터를 크롤링 후 저장

- 두 번째, 데이터를 토대로 그래프 및 테이블을 작성

- 세 번째, 작성한 그래프, 테이블로 PPT 보고서를 제작 

- 마지막, Sender가 Receiver들에게 SendMail 클래스를 통하여 이메일을 전송

![image](https://github.com/ninji0815/stock-report/assets/150305171/b649b61f-435a-4290-8a2d-9f64d9787f65)

## 📄 파일별 구현 형태








