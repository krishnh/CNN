import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("michaelverma0141@gmail.com","michaelverma16034619")
message=("MODEL BUILT CORRECTLY !!!")
s.sendmail("michaelverma01416@gmail.com","hemant.krishnatrey@gmail.com",message)


