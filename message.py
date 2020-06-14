import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("jyotididwania636@gmail.com","Milindverma@123")
message=("MODEL BUILT CORRECTLY !!!")
s.sendmail("jyotididwania636@gmail.com","hemant.krishnatrey@gmail.com",message)

