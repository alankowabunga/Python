'''
1.使用email.message模組建立內容
2.使用smpt模組建立內容
3.驗證寄件人身分:帳號密碼/兩階段驗證

建立訊息物件:
msg=email.message.EmailMessage()
利用訊息物件建立基本設定
msg["from"]="寄件人地址"
msg["to"]="收寄人地址"
msg["subject"]="標題"

#加入純文字訊息: msg.set_content("文字內容")

#加入HTML內容: msg.add_alternative("<h3>內容</h3>",subtype="html")

連線到smpt司服器:
import smtlib
#可以從網路上找到主機名稱和連接port number
server=smtplib.SMTP_SSL("主機名稱",連接 PORT number)
serber.login("account","password")

#發送訊息:send_message
server.send_message(msg)
server.close() #發送完畢後關閉連線

'''