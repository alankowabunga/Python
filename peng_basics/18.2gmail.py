import email.message
msg=email.message.EmailMessage()
msg["from"]="chnyujen0218@gmail.com"
msg["to"]="babyalan0857@gmail.com"
msg["subjct"]="Hello test test"

#msg.set_content("I am Alan") #純文字內容
msg.add_alternative("<h3>This is html</h3>",subtype="html")

#連線到 SMTP Server，驗證寄件人身分並發送郵件
import smtplib
#在網路上尋找 gmail smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("chenyujen0218@gmail.com","googlep@ssw0rd")
server.send_message(msg)
server.close()