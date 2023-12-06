
# 이메일 메시지에 다양한 형식을 중첩하여 담기 위한 객체
from email.mime.multipart import MIMEMultipart

# 이메일 메시지를 이진 데이터로 바꿔주는 인코더
from email import encoders

# 텍스트 형식
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio

from email.mime.base import MIMEBase

import smtplib
import os

#  sender 클래스에서 id, pw 등의 정보를 가져오기 위해 import
from sender import sender 
#  receiver 클래스에서 수신자 정보를 가져오기 위해 import
from receiver import receiver
    
### start here
class SendMail(sender, receiver):
    
    def __init__(self,ppt,today):
        super().__init__()  # 상위 클래스(sender, receiver)의 __init__ 메서드 호출
        self.receivers = ["wlgp5682@naver.com", "ninji0815@naver.com"]
### end here        
        self.smtp_dict = dict({"smtp_server" : "smtp.naver.com", # SMTP 서버 주소
                        "smtp_user_id" : self.id,
                        "smtp_user_pw" : self.pw,
                        "smtp_port" : 587}) # SMTP 서버 포트

        self.msg_dict = {
            'application' : {'maintype' : 'application', 'subtype' : 'octect-stream', 'filename' : 'res/email_sending/test.pdf'} # 그외 첨부파일
        }
        # 메일 내용 작성
        title = '({date}). Stock Report Analysis Data.'.format(date=today)
        content ='Stock Report Analysis Data.'
        sender = self.smtp_dict['smtp_user_id']

        msg = MIMEText(_text = content, _charset = "utf-8")

        # 첨부파일 추가
        self.msg_dict['application']['filename'] = ppt
        self.make_multimsg(self.msg_dict)
        self.multi['Subject'] = title
        self.multi['From'] = sender
        self.multi.attach(msg)

               
    def send_email(self):
            with smtplib.SMTP(self.smtp_dict["smtp_server"], self.smtp_dict["smtp_port"]) as server:
                # TLS 보안 연결
                server.starttls()
                # 로그인
                server.login(self.smtp_dict["smtp_user_id"], self.smtp_dict["smtp_user_pw"])

                # 로그인 된 서버에 이메일 전송
                response = server.sendmail(self.multi['from'],self.receivers,self.multi.as_string()) 

                # 이메일을 성공적으로 보내면 결과는 {}
                if not response:
                    print('이메일을 성공적으로 보냈습니다.')
                else:
                    print(response)

    def make_multimsg(self,msg_dict):
            self.multi = MIMEMultipart(_subtype='mixed')

            for key, value in msg_dict.items():
                # 각 타입에 적절한 MIMExxx() 함수를 호출하여 msg 객체를 생성.
                if key == 'text':
                    with open(value['filename'], encoding='utf-8') as fp:
                        msg = MIMEText(fp.read(), _subtype=value['subtype'])
                elif key == 'image':
                    with open(value['filename'], 'rb') as fp:
                        msg = MIMEImage(fp.read(), _subtype=value['subtype'])
                elif key == 'audio':
                    with open(value['filename'], 'rb') as fp:
                        msg = MIMEAudio(fp.read(), _subtype=value['subtype'])
                else:
                    with open(value['filename'], 'rb') as fp:
                        msg = MIMEBase(value['maintype'], _subtype=value['subtype'])
                        msg.set_payload(fp.read())
                        encoders.encode_base64(msg)

                # 경로가 있는 경우, 파일의 이름만 추출 ex) res/stock_report/stock_report.pptx -> stock_report.pptx
                _, fname = os.path.split(value['filename'])
                # 파일 이름을 첨부파일 제목으로 추가
                msg.add_header('Content-Disposition', 'attachment', filename = fname)

                # 첨부파일 추가
                self.multi.attach(msg)
                
# ###으로 표시한 부분 외에 전체적으로 코드 재구성 함.