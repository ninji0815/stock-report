
from pptx import Presentation
from pptx.util import Inches
import os

### start here

class MakeReport():    
    def __init__(self):
        # 파워포인트 객체 선언
        self.ppt = Presentation() 

    # 제목 슬라이드 추가
    def add_title(self,title_,subtitle_,provider_):
### end here
        # slide_layouts[0]: 제목 슬라이드에 해당
        title_slide = self.ppt.slide_layouts[0] 
        # 제목 슬라이드를 파워포인트 객체에 추가
        slide = self.ppt.slides.add_slide(title_slide) 

        left = Inches(0.5)
        top = Inches(2)
        pic = slide.shapes.add_picture("mark.gif",left,top)

        # 제목 - 제목에 값넣기
        title = slide.shapes.title # 제목
        title.text = title_ # 제목에 값 넣기

        # 부제목
        # 제목 상자는 placeholders[0], 부제목 상자는 [1]
        subtitle = slide.placeholders[1] 
        subtitle.text = subtitle_

        provider = slide.placeholders[1] 
        provider.text = provider_


        
    # 차트 및 테이블 슬라이드 추가   
    def add_table_chart(self,text_, chart_name_, table_name_):
        title_chart = self.ppt.slide_layouts[5]
        slide = self.ppt.slides.add_slide(title_chart)

        shapes = slide.shapes
        shapes.title.text = text_
        print(shapes.title.text)

        # 차트 추가
        left = Inches(0.5)
        height = Inches(2.5)
        width = Inches(9)
        top = Inches(2)

        chart_name = chart_name_
        chart_picture = slide.shapes.add_picture(chart_name, left, top, width=width, height=height)

        # 테이블 추가
        left = Inches(-1)
        height = Inches(3)
        width = Inches(12)
        top = Inches(4)

        table_name = table_name_
        table_picture = slide.shapes.add_picture(table_name, left, top, width=width, height=height)


    #보고서 저장
    def save_report(self):
        ppt_name = os.path.join("C:/Users/user/OneDrive - pusan.ac.kr/바탕 화면/stock_report" , 'stock_report.pptx')

### start here
        try:
            # PPT 저장
            self.ppt.save(ppt_name)
            print("PPT 저장 성공")
        except Exception as e:
            # 저장 중 오류 발생 시 오류 메시지 출력
            print(f"PPT 저장 실패: {e}")
        return ppt_name
    
### end here